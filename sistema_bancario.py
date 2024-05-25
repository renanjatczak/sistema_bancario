import os

def limpar_tela():
    os.system('cls')

saldo = 0.0
extrato = ""
saques_diarios = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500.00

while True:
    limpar_tela()
    print("\n--- Menu ---")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        limpar_tela()
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")
        input("Pressione Enter para continuar...")

    elif opcao == '2':
        limpar_tela()
        if saques_diarios < LIMITE_SAQUES:
            valor = float(input("Digite o valor do saque: "))
            if valor > 0:
                if valor <= LIMITE_SAQUE_VALOR:
                    if valor <= saldo:
                        saldo -= valor
                        extrato += f"Saque: -R${valor:.2f}\n"
                        saques_diarios += 1
                        print(f"Saque de R${valor:.2f} realizado com sucesso.")
                    else:
                        print("Saldo insuficiente para saque.")
                else:
                    print(f"O valor máximo para saque é R${LIMITE_SAQUE_VALOR:.2f}.")
            else:
                print("Valor de saque deve ser positivo.")
        else:
            print("Limite de 3 saques diários atingido.")
        input("Pressione Enter para continuar...")

    elif opcao == '3':
        limpar_tela()
        print("\n--- Extrato ---")
        if extrato:
            print(extrato)
        else:
            print("Nenhuma operação realizada.")
        print(f"Saldo atual: R${saldo:.2f}")
        input("Pressione Enter para continuar...")

    elif opcao == '4':
        print("Saindo...")
        break
        
    else:
        limpar_tela()
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")
