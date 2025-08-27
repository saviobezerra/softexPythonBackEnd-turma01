
n = int(input('Digite quantos quadriláteros você deseja calcular a área: '))
for i in range(n):
    lado=float(input(f'Digite o lado (em cm) do {i+1}° quadrilátero: '))
    print(f'A área do quadrilátero {i+1} é {lado*lado} cm²')

    