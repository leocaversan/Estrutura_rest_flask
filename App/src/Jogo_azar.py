import random


class JogoAzarManager:
    def __init__(self):
        self.resposta = Jogo_azar.gera_resposta()
    def gera_nova_resposta(self):
        self.resposta = Jogo_azar.gera_resposta()

class Jogo_azar():

    def __init__(self):
        '''O jogo gera um numero aleatorio e vai dando dicas até que acerte.'''
        
    def main(chute, response):
        chute_ = int(chute)
        resposta = int(response)
        
        if chute_ > resposta:
            return f"Errou! É um valor menor que {chute}"
        elif chute_ < resposta:
            return f"Errou! É um valor maior que {chute}"
        else:
            return f"Parabéns! O número gerado foi {response}"

    
    def gera_resposta():
        resposta = random.randint(1,9)
        return resposta


    
