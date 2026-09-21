import os
import mysql.connector
import pandas as pd

from dotenv import load_dotenv

load_dotenv()


def conectar():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return conexao


def buscar_vendas():
    conexao = conectar()

    consulta = """
        SELECT
            Cliente,
            Destino,
            País,
            Valor,
            Passageiros
        FROM vendas_viagens
    """

    df = pd.read_sql(consulta, conexao)

    conexao.close()

    return df

if __name__ == "__main__":
    conexao = conectar()

    if conexao.is_connected():
        print("Conectado ao MySQL com sucesso!")

    conexao.close()

def buscar_destinos():
    conexao = conectar()

    cursor = conexao.cursor()

    consulta = """
        SELECT DISTINCT Destino
        FROM vendas_viagens
        WHERE Destino IS NOT NULL
          AND Destino <> ''
        ORDER BY Destino
    """

    cursor.execute(consulta)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    destinos = [linha[0] for linha in resultados]

    return destinos