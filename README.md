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
