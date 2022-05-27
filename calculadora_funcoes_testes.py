import unittest
from calculadora_funcoes import *

class TesteFuncoes(unittest.TestCase):
    
    def teste_soma_inteiros(self):
        self.assertEqual(soma(5,5), 10)
        self.assertEqual(soma(5,10), 15)
        self.assertEqual(soma(1000,380), 1380)
        self.assertEqual(soma(20,964), 984)

    def teste_soma_decimais(self):
        self.assertEqual(soma(2.50,2.50), 5)
        self.assertEqual(soma(5.25,10.25), 15.50)
        self.assertEqual(soma(1000.45,380.30), 1380.75)
        self.assertEqual(soma(20.80,964.20), 985)

    def teste_subtracao_inteiros(self):
        self.assertEqual(subtracao(5,5), 0)
        self.assertEqual(subtracao(5,10), -5)
        self.assertEqual(subtracao(1000,380), 620)
        self.assertEqual(subtracao(20,964), -944)

    def teste_subtracao_decimais(self):
        self.assertEqual(subtracao(2.50,2.50), 0)
        self.assertEqual(subtracao(5.25,10.25), -5)
        self.assertEqual(subtracao(964.20,20.20), 944)

    def teste_multiplicacao_inteiros(self):
        self.assertEqual(multiplicacao(5,5), 25)
        self.assertEqual(multiplicacao(5,10), 50)
        self.assertEqual(multiplicacao(1000,380), 380000)
        self.assertEqual(multiplicacao(20,964), 19280)

    def teste_multiplicacao_decimais(self):
        self.assertEqual(multiplicacao(2.50,2.50), 6.25)
        self.assertEqual(multiplicacao(5.25,4), 21)
        self.assertEqual(multiplicacao(20,964.20), 19284)

    def teste_divisao_inteiros(self):
        self.assertEqual(divisao(5,5), 1)
        self.assertEqual(divisao(5,10), 0.5)
        self.assertEqual(divisao(1000,250), 4)
        self.assertEqual(divisao(964,20), 48.20)

    def teste_divisao_decimais(self):
        self.assertEqual(divisao(2.50,2.50), 1)
        self.assertEqual(divisao(10.50, 2), 5.25)

    def teste_exponenciacao_inteiros(self):
        self.assertEqual(exponenciacao(5,5), 3125)
        self.assertEqual(exponenciacao(5,10), 9765625)

    def teste_exponenciacao_decimais(self):
        self.assertEqual(exponenciacao(5.5, 2), 30.25)
        self.assertEqual(exponenciacao(10.5,2), 110.25)

    def teste_raizQuadrada_inteiros(self):
        self.assertEqual(raizQuadrada(16), 4)
        self.assertEqual(raizQuadrada(144), 12)
        self.assertEqual(raizQuadrada(256), 16)

    def teste_logaritmo_inteiros(self):
        self.assertEqual(logaritmo(10), 1)
        self.assertEqual(logaritmo(8), 0.9030899869919435)
        self.assertEqual(logaritmo(100), 2)
        self.assertEqual(logaritmo(150), 2.1760912590556813)
        self.assertEqual(logaritmo(1000), 3)