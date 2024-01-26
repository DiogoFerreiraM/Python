import random

print('Bem vindo ao jogo de advinhação')
numero_secreto = random.randrange(1,11)

print(numero_secreto)

rodada = 1
tentativa = 4


while (rodada <= tentativa):
    print(f'Tentativa {tentativa} de {rodada}')
    
    escolha = input('tente advinhar o numero secreto: ')
    escolha_int = int((escolha))

    acertou = numero_secreto == escolha_int
    menor = numero_secreto < escolha_int
    maior = numero_secreto > escolha_int

    if (acertou):
        print('Voce acertou')
        break
    else:
        if (maior):
            print('\no numero secreto é maior que o digitado\n')
        elif (menor):
            print('\no numero secreto é menor que o digitado\n')
    rodada = rodada + 1 

print('fim de jogo')