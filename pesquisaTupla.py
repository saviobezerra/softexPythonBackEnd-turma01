# 15. Pesquisa em tupla
# Crie uma tupla com números e verifique se um número digitado pelo usuário está dentro da tupla.


tupla=(1,2,3,5,7,12,19,31)
x=0


while(x not in tupla):
    x = int(input('Digite um número: '))
    if x in tupla:
        print('Está  na tupla!')
    else:
        print('Não está na tupla!')