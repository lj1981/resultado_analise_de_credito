import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE
import joblib
import re
import os
import warnings


def clean_currency(value):
    """Função melhorada para limpar valores monetários"""
    if pd.isna(value) or value == '':
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)

    # Remove símbolos de moeda, espaços e trata separadores decimais
    value = str(value).strip()
    value = re.sub(r'[^\d,]', '', value)  # Mantém apenas dígitos e vírgulas
    value = value.replace('.', '').replace(',', '.')  # Converte para formato decimal

    try:
        return float(value)
    except:
        return np.nan


def main():
    try:
        # 1. Carregar os dados
        file_path = '/home/luiz/Downloads/Projetos_One/analise_credito/dataset_credito_simulado.csv'
        print(f"\nCarregando dados de: {file_path}")

        df = pd.read_csv(file_path, encoding='utf-8', delimiter=',')
        df.columns = df.columns.str.strip()

        # Verificar se as colunas esperadas existem
        required_cols = ['Salário', 'Patrimônio', 'Parcelas_Médias', 'Estado', 'Cidade', 'Bairro', 'Status']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Colunas obrigatórias faltando: {missing_cols}")

        print("\nDados carregados com sucesso. Primeiras linhas:")
        print(df.head().to_string())

        # 2. Pré-processamento de colunas numéricas
        numeric_cols = ['Salário', 'Patrimônio', 'Parcelas_Médias']
        for col in numeric_cols:
            df[col] = df[col].apply(clean_currency)
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # 3. Verificação de valores faltantes
        print("\nValores faltantes antes da imputação:")
        print(df[numeric_cols].isna().sum())

        # 4. Imputação mais inteligente (corrigida para evitar o warning)
        for col in numeric_cols:
            if df[col].isna().all():  # Se TODOS os valores estão faltando
                print(f"\nERRO CRÍTICO: Coluna '{col}' não tem nenhum valor válido.")
                # Como contingência, vamos usar valores aleatórios baseados em distribuições realistas
                if col == 'Salário':
                    df[col] = np.random.normal(3000, 1500, len(df)).round(2)
                elif col == 'Patrimônio':
                    df[col] = np.random.normal(20000, 10000, len(df)).round(2)
                elif col == 'Parcelas_Médias':
                    df[col] = np.random.uniform(0, 1000, len(df)).round(2)
            else:
                # Imputação baseada na mediana (menos sensível a outliers)
                median = df[col].median()
                df[col] = df[col].fillna(median)  # Forma correta sem warning

        print("\nEstatísticas após imputação:")
        print(df[numeric_cols].describe())

        # 5. Engenharia de features
        # Criar novas features que podem ser úteis
        df['Salário_Patrimônio_Ratio'] = df['Salário'] / (df['Patrimônio'] + 1)  # +1 para evitar divisão por zero
        df['Endividamento'] = df['Parcelas_Médias'] / (df['Salário'] + 1)

        # 6. Codificação de categorias com get_dummies
        categorical_cols = ['Estado', 'Cidade', 'Bairro']
        df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

        # 7. Verificar balanceamento das classes
        print("\nDistribuição das classes de Status:")
        print(df['Status'].value_counts())

        # 8. Preparação dos dados para modelagem
        # Lista de colunas para remover (ajuste conforme seu dataset)
        cols_to_drop = ['ID', 'Nome', 'Gênero', 'Empréstimo', 'Financiamento', 'Score', 'Crédito_Pre_Aprovado']
        X = df.drop(['Status'] + [col for col in cols_to_drop if col in df.columns], axis=1)
        y = df['Status']

        # 9. Balanceamento das classes com SMOTE
        smote = SMOTE(random_state=42)
        X_res, y_res = smote.fit_resample(X, y)

        # 10. Divisão dos dados
        X_train, X_test, y_train, y_test = train_test_split(
            X_res, y_res, test_size=0.2, random_state=42, stratify=y_res)

        # 11. Modelagem com pipeline
        model = make_pipeline(
            StandardScaler(),
            RandomForestClassifier(
                n_estimators=200,
                class_weight='balanced',
                random_state=42,
                max_depth=10,
                min_samples_split=5
            )
        )

        model.fit(X_train, y_train)

        # 12. Avaliação
        print("\nAvaliação do Modelo:")
        print(classification_report(y_test, model.predict(X_test)))

        # 13. Feature Importance
        rf = model.named_steps['randomforestclassifier']
        feature_importances = pd.DataFrame({
            'Feature': X.columns,
            'Importance': rf.feature_importances_
        }).sort_values('Importance', ascending=False)

        print("\nImportância das Features:")
        print(feature_importances.to_string())

        # 14. Salvar modelo e feature names
        joblib.dump({
            'model': model,
            'feature_names': list(X.columns),
            'preprocessing_info': {
                'numeric_cols': numeric_cols,
                'categorical_cols': categorical_cols
            }
        }, 'modelo_credito_melhorado.pkl')

        print("\nModelo treinado salvo com sucesso como 'modelo_credito_melhorado.pkl'")

    except Exception as e:
        print(f"\nERRO: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # Opcional: Filtrar warnings específicos se necessário
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=UserWarning)
    main()