import random
import statistics
import numpy as np
import pandas as pd

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

def preparar_dados(df):
    df["Valor"] = pd.to_numeric(df["Valor"])
    df["Passageiros"] = pd.to_numeric(df["Passageiros"])

    return df


def relatorio_geral(df):

    df = preparar_dados(df)

    quantidade_vendas = len(df)

    faturamento_total = np.sum(df["Valor"])

    ticket_medio = statistics.mean(df["Valor"])

    maior_venda = np.max(df["Valor"])

    menor_venda = np.min(df["Valor"])

    destino_mais_vendido = (
        df["Destino"]
        .value_counts()
        .idxmax()
    )

    faturamento_destino = (
        df.groupby("Destino")["Valor"]
        .sum()
    )

    destino_maior_faturamento = faturamento_destino.idxmax()

    total_passageiros = np.sum(df["Passageiros"])

    vendas_acima_media = df[
        df["Valor"] > ticket_medio
    ]

    cliente_maior_compra = df.loc[
        df["Valor"].idxmax(),
        "Cliente"
    ]

    # Uso da biblioteca random exigida pelo exercício
    venda_aleatoria = random.choice(
        df["Cliente"].tolist()
    )

    return {
        "quantidade_vendas": quantidade_vendas,
        "faturamento_total": faturamento_total,
        "ticket_medio": ticket_medio,
        "maior_venda": maior_venda,
        "menor_venda": menor_venda,
        "destino_mais_vendido": destino_mais_vendido,
        "destino_maior_faturamento": destino_maior_faturamento,
        "total_passageiros": total_passageiros,
        "vendas_acima_media": vendas_acima_media,
        "cliente_maior_compra": cliente_maior_compra,
        "venda_aleatoria": venda_aleatoria
    }

def vendas_acima_ticket_medio(df):

    df = preparar_dados(df.copy())

    ticket_medio = df["Valor"].mean()

    vendas = df[
        df["Valor"] > ticket_medio
    ].copy()

    return {
        "ticket_medio": float(ticket_medio),
        "vendas": vendas.to_dict(orient="records")
    }

def consultar_destino(df, destino):

    df = preparar_dados(df)

    resultado = df[
        df["Destino"].str.lower() == destino.lower()
    ]

    if resultado.empty:
        return None

    quantidade = len(resultado)

    faturamento = resultado["Valor"].sum()

    ticket_medio = resultado["Valor"].mean()

    passageiros = resultado["Passageiros"].sum()

    return {
        "destino": destino,
        "quantidade": quantidade,
        "faturamento": faturamento,
        "ticket_medio": ticket_medio,
        "passageiros": passageiros,
        "vendas": resultado
    }

def gerar_graficos(df):

    df = preparar_dados(df)

    faturamento = (
        df.groupby("Destino")["Valor"]
        .sum()
        .sort_values(ascending=False)
    )

    vendas = (
        df["Destino"]
        .value_counts()
    )

    # ----------------------------------
    # Gráfico 1 - Seaborn
    # Faturamento por destino
    # ----------------------------------

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=faturamento.index,
        y=faturamento.values
    )

    plt.title("Faturamento por destino")
    plt.xlabel("Destino")
    plt.ylabel("Faturamento")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "static/graficos/faturamento_destino.png"
    )

    plt.close()


    # ----------------------------------
    # Gráfico 2 - Matplotlib
    # Quantidade de vendas
    # ----------------------------------

    plt.figure(figsize=(10, 6))

    plt.bar(
        vendas.index,
        vendas.values
    )

    plt.title("Quantidade de vendas por destino")
    plt.xlabel("Destino")
    plt.ylabel("Quantidade")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "static/graficos/vendas_destino.png"
    )

    plt.close()


    # ----------------------------------
    # Gráfico 3 - Pizza
    # ----------------------------------

    plt.figure(figsize=(8, 8))

    plt.pie(
        faturamento.values,
        labels=faturamento.index,
        autopct="%1.1f%%"
    )

    plt.title(
        "Participação do faturamento por destino"
    )

    plt.tight_layout()

    plt.savefig(
        "static/graficos/participacao_faturamento.png"
    )

    plt.close()

