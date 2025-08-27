#1 - criacao de lista simples
lista=[1,2,3,4,5]
print(f'Questão 1: {lista}')

#2 - lista cores e printar segunda e última cor
cores=['azul','verde','vermelho','amarelo']
print(f'Questão 2: {cores[1]} e {cores[-1]}')

#3 - alteração de elemento
frutas=['banana','maçã','kiwi']
frutas[0]='morango'
print(f'Questão 3: {frutas}')

#4 - adicionando elementos
lista=[]
for i in range(5):
    x=int(input('Digite um numero: '))
    lista.append(x)
print(f'Questão 4: {lista}')

#5 - ordenar em valores crescentes
listaNum = [8,3,10,1,7]
listaNum.sort()
print(f'Questão 5: {listaNum}')

#6 - somar elementos listas
listaSoma = []
for i in range (5):
    num = int(input('Digite um número: '))
    listaSoma.append(num)
print(f'Questão 6: Soma dos elementos da lista é: {sum(listaSoma)}')

#7 - maior e menor dos elementos
listaMaxMin = []
for i in range (5):
    num = int(input('Digite um número: '))
    listaMaxMin.append(num)
maior=max(listaMaxMin)
menor=min(listaMaxMin)
print(f'Questão 7: O maior número da lista é {maior} e o menor é {menor}')

#8 - contagem de letras
letras = ['a','b','a','c','a','d']
contaA = 0
for letra in letras:
    if letra=='a':
        contaA+=1
print(f'Questão 8: A lista {letras} tem {contaA} letras a')

#9 - funcao remove
numeros=[2,4,6,8,10]
numeros.remove(6)
print(f'Questão 9: A lista agora é:  {numeros}')
