# -*- coding: utf-8 -*-
# Meu nome: Sávio

def exibir_menu():
    
    print("""
===== MEU SISTEMA BANCÁRIO =====
1 - Depositar
2 - Sacar
3 - Fazer PIX
4 - Consultar Extrato
0 - Encerrar Sessão
================================
""")

saldo = 1000.00
limite_saque_diario = 500.00
extrato = []
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

# L para manter o programa rodando
while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    # Opção 1: Depósito
    if opcao == "1":
        print("--- Depósito ---")
        try:
            valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato.append(f"Depósito: + R$ {valor_deposito:.2f}")
                print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                print("\nErro: O valor do depósito precisa ser positivo.")
        except ValueError:
            print("\nErro: Eu preciso que você digite um número válido.")

    # Opção 2: Saque
    elif opcao == "2":
        print("--- Saque ---")
        try:
            valor_saque = float(input("Digite o valor a ser sacado: R$ "))
            
            # validações para o saque
            excedeu_saldo = valor_saque > saldo
            excedeu_limite_valor = valor_saque > limite_saque_diario
            excedeu_limite_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

            if excedeu_saldo:
                print("\nErro: Você não tem saldo suficiente.")
            elif excedeu_limite_valor:
                print(f"\nErro: O valor do saque é maior que seu limite de R$ {limite_saque_diario:.2f}.")
            elif excedeu_limite_saques:
                print(f"\nErro: Você já atingiu o limite de {LIMITE_SAQUES_DIARIOS} saques diários.")
            elif valor_saque > 0:
                saldo -= valor_saque
                numero_saques += 1
                extrato.append(f"Saque:    - R$ {valor_saque:.2f}")
                print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")
            else:
                print("\nErro: Valor de saque inválido.")
        except ValueError:
            print("\nErro: Eu preciso que você digite um número válido.")
    
    # Opção 3: PIX
    elif opcao == "3":
        print("--- Fazer PIX ---")
        try:
            chave_pix = input("Digite a chave PIX de destino: ")
            valor_pix = float(input(f"Digite o valor a ser enviado para '{chave_pix}': R$ "))

            if valor_pix <= 0:
                print("\nErro: O valor do PIX deve ser maior que zero.")
            elif valor_pix > saldo:
                print("\nErro: Saldo insuficiente para fazer este PIX.")
            else:
                saldo -= valor_pix
                extrato.append(f"PIX Enviado para '{chave_pix}': - R$ {valor_pix:.2f}")
                print(f"\nPIX de R$ {valor_pix:.2f} para '{chave_pix}' realizado com sucesso!")
        except ValueError:
            print("\nErro: Valor inválido, por favor, digite um número.")

    # Opção 4: Extrato
    elif opcao == "4":
        print("\n======= MEU EXTRATO BANCÁRIO =======")
        if not extrato:
            print("Nenhuma movimentação foi realizada ainda.")
        else:
            for movimento in extrato:
                print(movimento)
        print("------------------------------------")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("====================================")

    # Opção 0: Sair
    elif opcao == "0":
        print("\nSessão encerrada. Obrigado por usar meu sistema!")
        break

    # Caso a opção seja inválida
    else:
        print("\nOpção inválida. Por favor, escolha uma das opções do menu.")