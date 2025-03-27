📌 Visão Geral
Este sistema automatizado realiza análise de crédito utilizando machine learning para classificar clientes como "aprovados" ou "negados" com base em suas informações financeiras e demográficas.

📋 Pré-requisitos
Python 3.8+

Bibliotecas listadas em requirements.txt

Arquivo CSV com dados dos clientes

📂 Estrutura do Projeto

/analise_credito/
│── /dados/
│   └── dataset_credito_simulado.csv  # Dados de entrada
│── /modelos/
│   └── modelo_credito.pkl            # Modelo treinado
│── analise_credito.py                # Script principal
│── correlacao.png                    # Matriz de correlação
│── README.md                         # Esta documentação
└── requirements.txt                  # Dependências

🔧 Instalação

1. git clone [URL_DO_REPOSITORIO]
cd analise_credito

2. Instale as dependências:

3. pip install -r requirements.txt

🛠 Configuração

Edite as variáveis no início do script principal conforme necessário:

# Caminho para o arquivo de dados
FILE_PATH = 'dados/dataset_credito_simulado.csv'

# Colunas necessárias
COLUNAS_NUMERICAS = ['Salário', 'Patrimônio', 'Parcelas_Médias']
COLUNAS_CATEGORICAS = ['Estado', 'Cidade', 'Bairro', 'Status']

🚀 Como Executar

python analise_credito.py

🔄 Fluxo de Processamento

1. Carregamento de Dados

Lê o arquivo CSV especificado

Remove espaços extras nos nomes das colunas

2. Pré-processamento

Limpeza de valores monetários (remove 'R$', converte vírgulas)

Conversão para tipos numéricos

Imputação de valores faltantes

3. Análise Exploratória

Gera matriz de correlação

Salva gráfico em correlacao.png

4. Modelagem Preditiva

Codifica variáveis categóricas

Divide dados em treino/teste

Treina modelo RandomForest

5. Avaliação

Gera relatório de classificação

Exibe matriz de confusão

6. Persistência

Salva modelo treinado em modelos/modelo_credito.pkl

📊 Entrada de Dados

O arquivo CSV deve conter no mínimo estas colunas:

- Salário: Valor numérico ou formato monetário (R$1,234.56)

- Patrimônio: Valor numérico ou formato monetário

- Parcelas_Médias: Número de parcelas (valor inteiro)

- Estado, Cidade, Bairro: Dados categóricos

- Status: (0 = Negado, 1 = Aprovado)

Exemplo de linha:

Salário,Patrimônio,Parcelas_Médias,Estado,Cidade,Bairro,Status
R$3,500.00,15000.00,5,SP,São Paulo,Moema,1

📤 Saída

1. Resultados do Modelo (console):

Relatório de classificação

Acurácia do modelo

Matriz de confusão

2. Arquivos Gerados:

modelo_credito.pkl: Modelo treinado

correlacao.png: Matriz de correlação

🛠️ Como Adicionar Novos Dados

Para classificar novos clientes, crie um DataFrame com a mesma estrutura:

novos_clientes = pd.DataFrame({
    'Salário': [4000, 2500],
    'Patrimônio': [18000, 8000],
    'Parcelas_Médias': [4, 6],
    'Estado': ['SP', 'RJ'],
    'Cidade': ['São Paulo', 'Rio de Janeiro'],
    'Bairro': ['Vila Olímpia', 'Copacabana']
})

# Carregar modelo
modelo = joblib.load('modelos/modelo_credito.pkl')

# Fazer previsões
previsoes = modelo.predict(novos_clientes)

⚠️ Solução de Problemas

Problema: Erro na imputação de valores
Solução: Verifique se as colunas numéricas contêm valores válidos

Problema: Erro ao gerar matriz de correlação
Solução: Confira se todas colunas numéricas foram convertidas corretamente


📈 Melhorias Futuras

- Adicionar validação cruzada

- Implementar tunagem de hiperparâmetros

- Criar interface gráfica

📄 Licença

Este projeto está licenciado sob a licença MIT.
   



