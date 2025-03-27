import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('Agg')  # Usar backend não interativo
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib
import re
import os


def clean_numeric(value):
    """Função para limpar e converter valores numéricos"""
    if pd.isna(value):
        return np.nan
    if isinstance(value, str):
        value = re.sub(r'[^\d.]', '', value.replace(',', '.'))
        try:
            return float(value)
        except:
            return np.nan
    return float(value)


def main():
    try:
        # 1. Carregar os dados
        file_path = '/home/luiz/Downloads/Projetos_One/analise_credito/dataset_credito_simulado.csv'
        print(f"\nCarregando dados de: {file_path}")

        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        print("\nDados carregados com sucesso. Primeiras linhas:")
        print(df.head().to_string())

        # 2. Pré-processamento de colunas numéricas
        numeric_cols = ['Salário', 'Patrimônio', 'Parcelas_Médias']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = df[col].apply(clean_numeric)
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # 3. Verificação de valores faltantes
        print("\nValores faltantes antes da imputação:")
        print(df[numeric_cols].isna().sum())

        # 4. Imputação de valores faltantes (versão robusta)
        for col in numeric_cols:
            if col in df.columns:
                if df[col].count() == 0:  # Se não há valores válidos
                    print(f"\nAtenção: Coluna '{col}' sem valores válidos. Preenchendo com 0.")
                    df[col] = 0
                else:
                    imputer = SimpleImputer(strategy='mean')
                    df[col] = imputer.fit_transform(df[[col]]).ravel()

        print("\nEstatísticas após imputação:")
        print(df[numeric_cols].describe())

        # 5. Verificação de colunas necessárias
        required_cols = numeric_cols + ['Estado', 'Cidade', 'Bairro', 'Status']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Colunas faltantes: {missing_cols}")

        # 6. Codificação de categorias
        categorical_cols = ['Estado', 'Cidade', 'Bairro', 'Status']
        for col in categorical_cols:
            if col in df.columns:
                df[col] = LabelEncoder().fit_transform(df[col].astype(str))

        # 7. Análise de correlação
        try:
            plt.figure(figsize=(10, 8))
            corr_matrix = df[required_cols].corr()
            sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
            plt.title("Matriz de Correlação")
            plt.savefig('correlacao.png')
            print("\nMatriz de correlação salva em 'correlacao.png'")
        except Exception as e:
            print(f"\nErro ao gerar matriz de correlação: {str(e)}")

        # 8. Modelagem
        X = df[['Salário', 'Patrimônio', 'Parcelas_Médias', 'Estado', 'Cidade', 'Bairro']]
        y = df['Status']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # 9. Avaliação
        print("\nAvaliação do Modelo:")
        print(classification_report(y_test, model.predict(X_test)))

        # 10. Salvar modelo
        joblib.dump(model, 'modelo_credito.pkl')
        print("\nModelo treinado salvo com sucesso como 'modelo_credito.pkl'")

    except Exception as e:
        print(f"\nERRO: {str(e)}")
        print("\nInformações para diagnóstico:")
        if 'df' in locals():
            print("\nTipos de dados:")
            print(df.dtypes)
            print("\nValores únicos em 'Salário':")
            print(df['Salário'].unique())
        else:
            print("DataFrame não foi carregado corretamente.")


if __name__ == "__main__":
    main()