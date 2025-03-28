 - Sistema de Análise de Crédito

📌 Visão Geral
Este projeto implementa um sistema completo de análise de crédito utilizando machine learning. O sistema processa dados financeiros, realiza limpeza e transformação dos dados, treina um modelo preditivo e avalia seu desempenho.

🛠️ Tecnologias Utilizadas

Python 3.8+

Pandas (Manipulação de dados)

Scikit-learn (Machine Learning)

Imbalanced-learn (Balanceamento de classes)

Matplotlib/Seaborn (Visualização)

Joblib (Serialização do modelo)

📋 Estrutura do Código

1. Pré-processamento dos Dados

def clean_currency(value):
    """Converte valores monetários para float"""
    # Implementação da limpeza...

2. Engenharia de Features

Criação de novas variáveis:

Salário_Patrimônio_Ratio

Endividamento

Codificação de variáveis categóricas (one-hot encoding)

3. Modelagem Preditiva

model = make_pipeline(
    StandardScaler(),
    RandomForestClassifier(n_estimators=200, ...)
)
4. Avaliação do Modelo
Métricas: precision, recall, f1-score

Matriz de confusão

Feature importance

🚀 Como Executar
Instalação das dependências:

bash
Copy
pip install -r requirements.txt

Execução do script:


python analise_credito.py

Saídas geradas:

modelo_credito_melhorado.pkl (Modelo treinado)

correlacao.png (Matriz de correlação)

⚙️ Configuração

Parâmetros Ajustáveis

# No código principal:
n_estimators = 200    # Número de árvores na Random Forest
test_size = 0.2       # Proporção para teste
random_state = 42     # Semente para reprodutibilidade

📊 Fluxo de Processamento

Carrega o dataset

Realiza limpeza dos dados

Trata valores faltantes

Cria novas features

Codifica variáveis categóricas

Balanceia as classes

Treina o modelo

Avalia o desempenho

Salva o modelo treinado

📝 Notas Importantes

O dataset deve conter as colunas especificadas

Valores monetários devem estar em formato compatível

Para produção, considerar adicionar logs e monitoramento

📈 Melhorias Futuras

Implementar API para predições em tempo real

Adicionar validação cruzada

Testar outros algoritmos (XGBoost, LightGBM)

Criar dashboard de monitoramento

📄 Licença
MIT License - Consulte o arquivo LICENSE para mais detalhes.
