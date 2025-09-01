# 12. Imutabilidade da tupla
# Explique o que acontece ao tentar alterar um elemento de uma tupla. Faça o teste no código.

tuplaTeste = (1,2,3)
print(tuplaTeste[1])
tuplaTeste[1] = 2
print(tuplaTeste[1])


# tuplaTeste[1] = 2
  #  ~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment

#Tuplas são imutaveis! Não pode mudar!