import unittest 
from gera_valor_aleatorio import gera_resposta
  
class TestStringMethods(unittest.TestCase):

    def test_gera_resposta(self): 
        resposta_gerada = gera_resposta()
        possiveis_numeros = list(range(1,10,1))
        message = 'numero gerado de forma incorreta'
        self.assertIn(resposta_gerada, possiveis_numeros, message)
    
if __name__ == '__main__':
    unittest.main()