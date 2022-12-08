import random
from gera_valor_aleatorio import gera_resposta

class Jogo_azar:

    def __init__(self):
        '''O jogo gera um numero aleatorio e vai dando dicas até que acerte.'''

        self.main()
        
    def main(self):
        resposta = int(gera_resposta())
        print(resposta)
        tentativa = 0
        print("\nPalpite gerado!")

        chute=0
        try:    
            while chute is not resposta:
                tentativa += 1
                chute = int(input("Qual seu chute: "))
                if chute > resposta:
                    print("Errou! É um valor menor que ", chute)
                elif chute < resposta:
                    print("Errou! É um valor maior que ", chute)
                else:
                    print("Parabéns! O número gerado foi ",resposta, \
                        "Acertou em ",tentativa," tentativas!")
        
        except Exception as e:
            print(e)
        

if __name__ == '__main__':    
    Jogo_azar()
    
