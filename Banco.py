menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha-> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input('Digite o valor que deseja depositar: '))

        if valor_deposito <= 0:
            print('Deposite uma quantia valida.')
            continue

        saldo += valor_deposito
        extrato += (f"Depósito: R$ {valor_deposito:.2f}\n")  # Adiciona o historico de depósito ao extrato
        print('Depositado com sucesso!')
    
    elif opcao == 's':
        valor_saque = float(input('Qual o valor que deseja sacar: '))

        if valor_saque <= saldo and valor_saque <= limite:

            if numero_saques >= LIMITE_SAQUES:
                print('Limite de saques exedido')
                break

            saldo -= valor_saque
            numero_saques += 1
            #print(numero_saques)
            extrato += (f"Saque: R$ {valor_saque:.2f}\n")  # Adiciona o historico de Saque ao extrato
            print('Saque realizado')
            
        else:
            print('Valor do saldo é menor')


    elif opcao == 'e':
        print('\n-------Extrato------')
        print(extrato)  # Exibe o histórico de transações
        print('--------------------')
        print(f"Saldo atual: R$ {saldo:.2f}")
        print('--------------------')
        
    elif opcao == 'q':
        break

    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')