(EN)

Data Analysis with Python

A project developed with a focus on data analysis using Python, with a local MySQL database as the data source.

The application allows users to query sales information from a travel agency, generate metrics, filter data by destination, and view dynamically generated charts.

Technologies used:

• Python • Flask • Pandas • NumPy • Matplotlib • Seaborn • MySQL • HTML5 • CSS3

Features:

Querying data stored in MySQL
General sales report
Calculation of total revenue
Calculation of average ticket
Identification of the highest and lowest sales
Identification of the best-selling destination
Identification of the destination with the highest revenue
Querying sales by destination
List of sales above the average ticket
Generation of charts using Matplotlib and Seaborn
Since this system uses a MySQL database running directly on the machine, it can only be tested locally—by my choice... However, so you can see it in action, click the link attached to the repository to access a video demonstrating it.

Project structure:

```text
TRAVEL/
│
├── app.py
├── analise.py
├── database.py
├── requirements.txt
├── .env
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── graficos/

```
(PT)

Data Analysis with Python

Projeto desenvolvido com foco em **Análise de Dados utilizando Python**, tendo como fonte de dados um **banco de dados MySQL local**.

A aplicação permite consultar informações de vendas de uma agência de viagens, gerar métricas, filtrar dados por destino e visualizar gráficos gerados dinamicamente.

Tecnologias utilizadas:

• Python
• Flask
• Pandas
• NumPy
• Matplotlib
• Seaborn
• MySQL
• HTML5
• CSS3

Funcionalidades:

- Consulta de dados armazenados em MySQL
- Relatório geral de vendas
- Cálculo de faturamento total
- Cálculo de ticket médio
- Identificação da maior e menor venda
- Identificação do destino mais vendido
- Identificação do destino com maior faturamento
- Consulta de vendas por destino
- Listagem de vendas acima do ticket médio
- Geração de gráficos com Matplotlib e Seaborn

Por usar um Banco de Dados MySQL direto na máquina, este sistema somente pode ser testado localmente, por escolha minha...
Todavia, para que você possa vê-lo funcionando, acesse o link em anexo no Repositório para ter acesso a um vídeo demonstrando-o.

Estrutura do projeto:

```text
TRAVEL/
│
├── app.py
├── analise.py
├── database.py
├── requirements.txt
├── .env
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── graficos/
