#Atividades para fixação

#Crie uma função que receba um número e retorne o seu quadrado.
def quadrado(n):
    return n ** 2

#Crie uma função que receba dois números e retorne o maior deles.
def maior(a, b):
    return a if a > b else b

#Crie uma função que receba uma lista de números e retorne a soma.
def soma_lista(lista):
    return sum(lista)

#Crie uma função que mostre a tabuada de um número.
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

#Use lambda para criar uma função que calcule o dobro de um número.
dobro = lambda x: x * 2


print(f'Questão 1: ')
x = int(input('Digite um número: '))
print(f'O quadrado de {x} é: {quadrado(x)}')

print(f'Questão 2: ')
a = int(input('Digite um número a: '))
b = int(input('Digite um número b: '))
print(f'O maior entre {a} e {b} é {maior(a,b)}')

print(f'Questão 3: ')
n = int(input('Digite o número de itens na lista: '))
lista = []
for i in range(n):
    item = int(input('Digite um número: '))
    lista.append(item)
print(f'A soma dos itens da lista é {soma_lista(lista)}')

print(f'Questão 4: ')
c = int(input('Digite um número: '))
tabuada(c)

print(f'Questão 5: ')
d = int(input('Digite um número: '))
print(f'O dobro de {d} é: {dobro(d)}')