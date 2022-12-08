from Jogo_azar import Jogo_azar
from flask import Flask

app = Flask(__name__)


@app.route("/jogo_azar")
def hello_world():
    Jogo_azar()
    return "Olá, voce acertou!"
    # return "<p>Parabens, vocë acertou!!</p>"

