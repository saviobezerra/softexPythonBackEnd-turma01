maior = 0
for i in range (5):
    x = int(input('Digite um número: '))
    if x>maior:
        maior=x
print(f'O maior número é {maior}')