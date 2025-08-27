def media(lista):
    media=sum(lista)/len(lista)
    return media

lista=[]
x=int(input('Quantos elementos terá a lista? '))
for i in range(x):
    novo=int(input('Digite um número: '))
    lista.append(novo)
print(f'A lista digitada foi {lista} A média é {media(lista)}')