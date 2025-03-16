Documento Técnico - Análise de Crédito com Dash e Plotly

Visão Geral
Este projeto tem como objetivo fornecer uma interface interativa para análise de crédito de um conjunto de dados simulados. Utilizando as bibliotecas Dash e Plotly, o script oferece gráficos dinâmicos e filtros interativos, permitindo a visualização de dados de crédito em tempo real. Ele foi projetado para ser facilmente executado por outros usuários que possuam o dataset necessário.

Requisitos
Para executar este script, o usuário deve ter o seguinte ambiente configurado:

Python 3.7+
Bibliotecas:
Pandas: para manipulação de dados.
Plotly: para criação de gráficos interativos.
Dash: para construção da interface interativa web.
Como instalar as dependências:
Recomenda-se usar um ambiente virtual para gerenciar as dependências. Siga as etapas abaixo:

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv

Ative o ambiente virtual:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

Instale as bibliotecas necessárias:


pip install pandas plotly dash

Estrutura do Código
O script é dividido em várias seções que podem ser explicadas da seguinte forma:

Carregamento de Dados: O código começa carregando um dataset de crédito simulado (CSV). O arquivo CSV contém informações como nome do cliente, status de crédito, salário, entre outros.

Funções de Preprocessamento: A função converter_moeda é utilizada para formatar colunas financeiras, como salário e empréstimos, no formato monetário brasileiro (R$).

Criação de Gráficos: Gráficos interativos são criados utilizando Plotly, com opções de visualização de distribuição de score de crédito, status de crédito e a relação entre salário e crédito pré-aprovado.

Interface com o Usuário (Dash): O Dash é utilizado para criar a interface web interativa, onde os usuários podem aplicar filtros para selecionar o status de crédito e o intervalo de score de crédito. O layout é composto por:

Dropdown para seleção de status de crédito.
RangeSlider para selecionar a faixa de score de crédito.
Gráficos interativos baseados nos filtros aplicados.
Execução do Servidor: O servidor Dash é iniciado, permitindo que o usuário interaja com os gráficos através de um navegador.

Como Executar o Script
1. Prepare o Dataset:
Antes de executar o script, certifique-se de ter o dataset no formato CSV com as seguintes colunas:

ID
Nome
Idade
Gênero
Estado
Cidade
Bairro
Salário
Patrimônio
Empréstimos de 3 meses (Empréstimo_Mês1, Empréstimo_Mês2, Empréstimo_Mês3)
Financiamento de 3 meses (Financiamento_Mês1, Financiamento_Mês2, Financiamento_Mês3)
Parcelas Médias
Score
Status (Ruim, Moderado, Bom, Excelente)
Crédito Pré-Aprovado

2. Modifique o Caminho do Arquivo:
Alterar o caminho do arquivo CSV no script para corresponder à localização do seu dataset:

caminho_arquivo = "caminho/do/seu/arquivo/dataset_credito_simulado.csv"

3. Execute o Script:
No terminal ou prompt de comando, navegue até a pasta onde o script está localizado e execute o arquivo Python:

python nome_do_script.py

4. Acesse o Dashboard:
Após a execução, o Dash estará rodando localmente. Abra um navegador e acesse o seguinte endereço:

http://127.0.0.1:8050/
Você verá a interface interativa com gráficos que podem ser filtrados conforme o seu desejo.

Funcionalidades do Dashboard
Dropdown para Status de Crédito: Permite filtrar os dados para exibir apenas informações de clientes com o status de crédito selecionado (Ruim, Moderado, Bom, Excelente).

RangeSlider para Score de Crédito: Permite ajustar um intervalo de score de crédito e visualizar os dados de clientes dentro dessa faixa.

Gráficos Interativos:

Distribuição do Score de Crédito: Exibe a distribuição de scores dos clientes.
Distribuição do Status de Crédito: Exibe a proporção de clientes em cada categoria de status de crédito.
Relação entre Salário e Crédito Pré-Aprovado: Exibe um gráfico de dispersão mostrando como o salário dos clientes se relaciona com o crédito pré-aprovado.
Exemplo de Uso
Aqui está um exemplo básico de como interagir com o dashboard:

Selecione o status "Excelente" no dropdown de status de crédito.
Ajuste o RangeSlider para exibir apenas clientes com score de crédito entre 600 e 800.
Observe como os gráficos são atualizados dinamicamente com base nesses filtros.
Customizações Possíveis
Alterar a aparência: Você pode modificar o estilo visual do Dash, incluindo cores, fontes e layout, utilizando CSS. Crie um arquivo CSS e aplique no projeto para personalizar ainda mais a interface.

Adicionar novos filtros: Caso você deseje adicionar mais filtros interativos (por exemplo, filtrando por cidade ou patrimônio), basta adicionar novos componentes Dash e atualizar a função de callback para incluir esses filtros.

Conclusão
Este script permite uma análise de crédito interativa utilizando Dash e Plotly. Ele pode ser facilmente adaptado para diferentes datasets ou requisitos de visualização. Aproveite os recursos interativos para explorar os dados de forma dinâmica e eficiente!
