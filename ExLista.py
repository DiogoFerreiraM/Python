"""
Exercício 5: Lista de Compras
Crie um programa que inicialmente apresenta uma lista vazia de compras. 
Em seguida, o programa deve oferecer ao usuário a opção de adicionar itens à lista, remover itens da lista ou imprimir a lista de compras. 
O programa termina quando o usuário escolhe sair.

"""
import os
import time

def mostrar_lista (lista):
    if lista:
        print('\nLista de compras: ')
    else:
        print('Lista vazia')
    for item in lista:
        print(f'-{item}')

def adicionar_item(lista):
    item = input('Digite o nome do item que deseja adicionar: ')
    lista.append(item)
    print('O item foi adicionado')

def remover_item(lista):
    item = input('Qual item gostaria de remover: ')
    if item in lista:
        lista.remove(item)
        print('O item foi removido da lista de compras!!')
    else:
        print('Item não encontrado.')

# Lista de compras vazia
lista = []

while True:

    print('\nPara visualizar a lista digite (1) ')
    print('Para adicionar um item na lista digite (2) ')
    print('Para Remover um item da lista digite (3) ')
    print('Para Sair digite (4) ')
    escolha = input('Digite qual a sua escolha: ')

    if escolha == '1':
        mostrar_lista(lista)
    elif escolha == '2':
        adicionar_item(lista)
    elif escolha == '3':
        remover_item(lista)
    elif escolha == '4':
        print('Saindo da Lista')
        time.sleep(1)
        os.system('cls')
        break
    else:
        print('Opção invalida, porfavor tente novamente')
        continue

