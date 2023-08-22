from App.src.Jogo_azar import Jogo_azar, JogoAzarManager
from flask import Flask, request

app = Flask(__name__)


jogo_manager = JogoAzarManager()

@app.post("/jogo_azar")
def game_bad_luck():
    chute = request.json.get('chute')
    result = Jogo_azar.main(chute, jogo_manager.resposta)
    return {
                "resultado": result
            }

@app.get("/gera_nova_resposta")
def generate_new_response():
    resposta = jogo_manager.gera_nova_resposta()
    return {
                "message": "Novo valor gerado com sucesso!", 
            }

@app.errorhandler(404)
def resource_not_found(e):
    return {
            "error":"Not found!",
            "message": 404
            }