from App.src.Jogo_azar import Jogo_azar
from flask import Flask, request

app = Flask(__name__)

resposta = Jogo_azar.gera_resposta()

@app.post("/jogo_azar")
def game_bad_luck():
    chute = request.json.get('chute')
    result = Jogo_azar.main(chute, resposta)
    return  {
                "resultado":(result)
            }
        
@app.route("/")
def hello_world():
    return {
        "username": "teste"
    }
@app.errorhandler(404)
def resource_not_found(e):
    return {
            "error":"Not found!",
            "message": 404
            }