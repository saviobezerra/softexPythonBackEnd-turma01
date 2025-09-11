#Atividades para fixação

import random
import datetime
import math
import requests


#Use a biblioteca random para sortear um número entre 1 e 100.
numero_sorteado = random.randint(1, 100)
print("Questão 1: Número sorteado: ", numero_sorteado)

#Crie uma lista de nomes e use random.choice() para escolher um vencedor.
nomes = ["Ana", "Sávio", "Natália", "Flaviano", "Klewerson"]
vencedor = random.choice(nomes)
print("Vencedor do sorteio: ", vencedor)

#Use a biblioteca datetime para mostrar a data e hora atuais.
agora = datetime.datetime.now()
print("Data e hora atuais:", agora.strftime("%d/%m/%Y %H:%M:%S"))


#Com math, calcule a potência de 2 elevado a 10.
potencia = math.pow(2, 10)
print("2 elevado a 10 é:", potencia)

#Instale a biblioteca requests e faça 
# uma requisição para o site https://www.google.com.
resposta = requests.get("https://www.google.com")
print("Status da requisição para Google:", resposta.status_code)