# Projeto locadora DE FILMES ONLINE com 4 funções (listagem, locação,
# devolução e encerramento do sistema)
# Multa por atraso. 

# OPÇÃO: 1 LISTAR OS FILMES
# OPÇÃO: 2 ALUGAR UM FILME
# OPÇÃO: 3 DEVOLVER UM FILME
# OPÇÃO: 4 SAIR

filmes = ['filme1', 'filme2', 'filme3']
alugados = {}   # dicionario
multa = 2.5     # multa por dia

while True:
    opcao = int(input(
        '\nBem Vindo à Locadora!\n'
        '1 - LISTAR OS FILMES\n'
        '2 - ALUGAR UM FILME\n'
        '3 - DEVOLVER UM FILME\n'
        '4 - SAIR\n'
        'Digite uma opção: \n'
    ))

    if opcao == 1: #listar os filmes
        print("\nFIlmes disponíveis: ")
        if not filmes:
            print("Nenhum filme disponível no momento.")
        else:
            for i, filme in enumerate(filmes, start=1):
                print(f"{i}. {filme}")

    elif opcao == 2: #alugar
        print("\nAlugar FIlme:")
        if not filmes:
            print("Nenhum filme disponível para alugar.")
        else:
            for i, filme in enumerate(filmes, start=1):
                print(f"{i}. {filme}")
            escolha = int(input("Digite o número do filme que deseja alugar: ")) - 1
            if 0 <= escolha < len(filmes):
                filme_escolhido = filmes.pop(escolha)
                dias = int(input("Por quantos dias pretende alugar? "))
                alugados[filme_escolhido] = dias
                print(f"Você alugou '{filme_escolhido}' por {dias} dias!")
            else:
                print("Opção inválida!")


    elif opcao == 3: #devolver
        print("\nDevolver Filme: ")
        if not alugados:
            print("Nenhum filme para devolver!")
        else:
            for i, filme in enumerate(alugados.keys(), start=1):
                print(f"{i}. {filme}")
            escolha = int(input("Digite o número do filme que deseja devolver: ")) - 1
            if 0 <= escolha < len(alugados):
                filme_escolhido = list(alugados.keys())[escolha]
                dias_previstos = alugados[filme_escolhido]
                dias_reais = int(input("Quantos dias você ficou com o filme? "))
                atraso = dias_reais - dias_previstos
                if atraso > 0:
                    valor_multa = atraso * multa
                    print(f"Atraso de {atraso} dia(s)! Multa: R${valor_multa:.2f}")
                else:
                    print("Devolução dentro do prazo!")
                    
                filmes.append(filme_escolhido)
                del alugados[filme_escolhido]
            else:
                print("Opção inválida!")

    
    elif opcao == 4: #sair
      break

    else:
        print("Opção inválida!")
