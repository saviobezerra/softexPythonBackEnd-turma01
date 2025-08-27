vogal=0
palavra = input('Digite uma string: ')
for letra in palavra:
    if letra=='a' or letra=='e' or letra =='i' or letra =='o' or letra =='u' or letra =='á' or letra =='é' or letra =='í' or letra =='ú':
        vogal+=1

print(f'{palavra} tem {vogal} vogais!')