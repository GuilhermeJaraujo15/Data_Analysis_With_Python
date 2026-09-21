from flask import Flask, render_template, request

from database import buscar_vendas, buscar_destinos

from analise import (
    relatorio_geral,
    consultar_destino,
    gerar_graficos,
    vendas_acima_ticket_medio
)


app = Flask(__name__)
@app.context_processor
def carregar_destinos():
    return {
        "destinos_disponiveis": buscar_destinos()
    }

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/relatorio-geral")
def relatorio():

    df = buscar_vendas()

    resultado = relatorio_geral(df)

    return render_template(
        "index.html",
        resultado=resultado
    )


@app.route("/vendas-acima-media")
def acima_media():

    df = buscar_vendas()

    resultado = vendas_acima_ticket_medio(df)

    return render_template(
        "index.html",
        acima_media=resultado
    )


@app.route("/consultar-destino")
def destino():

    nome_destino = request.args.get("destino")

    if not nome_destino:
        return render_template(
            "index.html",
            erro="Informe um destino."
        )

    df = buscar_vendas()

    resultado_destino = consultar_destino(
        df,
        nome_destino
    )

    return render_template(
        "index.html",
        destino=resultado_destino
    )


@app.route("/graficos")
def graficos():

    df = buscar_vendas()

    gerar_graficos(df)

    return render_template(
        "index.html",
        graficos=True
    )


if __name__ == "__main__":
    app.run(debug=True)