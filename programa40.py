# x1 = input('Digide a primeira palavra: ')
# x2 = input('Digite a segunda palavra: ')
# print(x1.upper(),x2.upper())
# print(x1 + x2)
# print(len(x1))
# print(x2[2:4])
# print(x1.split(' '))
# print(x1.strip())
# print(x1.replace('h', 'j'))
#--------------------------------------------------------------------------------------------------------------------------------
# x1 = int(input('Digite um valor: '))
# x2 = int(input('Digite outro valor: '))
# print(x1 + x2)
# x1 *= 3
# print(x1)
# x2 += 2
# print(x2)
# x3 = x1 % x2
# print(x3)
#--------------------------------------------------------------------------------------------------------------------------------
# v1 = int(input('Digite um valor: '))
# for n in range(1,11):
#     v2 = v1 * n
#     print(v2)
#--------------------------------------------------------------------------------------------------------------------------------
# lista = ["apple", "banana", "cherry"]
# print(lista) #pode ser mudado
# lista.append("orange") #adiciona
# print(lista)
# lista.remove("banana") #remove
# print(lista)
# tupla = {"apple", "banana", "cherry"} #não pode ser mudado
# print(tupla)
# set = {"apple", "banana", "cherry"}
# dicionario = {"brand": "ford", "model": "mustang"}
# print(dicionario["brand"])
#--------------------------------------------------------------------------------------------------------------------------------
# lista = []
# lista.append(input('Digite um produto: '))
# lista.append(input('Digite um produto: '))
# lista.append(input('Digite um produto: '))
# print(lista[1][1:3])
# print(lista)
# lista.pop(0)
# print(lista)
#--------------------------------------------------------------------------------------------------------------------------------
# nome = str(input('Qual o seu nome: '))
# lista = nome.split(' ')
# print(lista[0])
# print(lista[len(lista) - 1])
#--------------------------------------------------------------------------------------------------------------------------------
# num = int(input('Digite um valor: '))
# if num % 2 == 0:
#     print('Esse numeor é par')
# else:
#     print('Esse numero é impar')
#--------------------------------------------------------------------------------------------------------------------------------
# maior = -9999
# menor = 99999
# for n in range(0,3):
#     num = int(input('digite um numero: '))
#     if num > maior:
#         maior = num
#     elif num < menor:
#         menor = num
# print(f'O maior numero é {maior}')
# print(f'O menor numeor é {menor}')
#-------------------------------------------------------------------------------------------------------------------------------
# while True:
#     v1 = int(input('Digite um valor: '))
#     v2 = int(input('Digite um valor: '))
#     opc = int(input('[1]Somar[2]Multiplicar\n[3]Maior\n[4]Novos Numeros\n[5] Sair do programa\nO que vc deseja fazer:'))
#     if opc == 5:
#         break
#     elif opc == 1:
#         print(f'A soma é igual a : {v1+v2}')
#     elif opc == 2:
#         print(f'O resultado da multiplicação é : {v1 * v2}')
#     elif opc == 3:
#         if v1 > v2:
#             print(f'O numero {v1} é maior que {v2}')
#         else:
#             print(f'O numero {v2} é maior que {v1}')
#--------------------------------------------------------------------------------------------------------------------------------
# v1 = int(input('Digite um valor: '))
# for n in range(1,11):
#     v2 = v1 * n
#     print(v2)
#--------------------------------------------------------------------------------------------------------------------------------
# num = int(input('Digite um valor: '))
# pa = int(input('Digite qual será a PA: '))
# for n in range(0,10):
#     num +=  pa
#     print(num)
#--------------------------------------------------------------------------------------------------------------------------------
# def saudacao(nome=''):
#     msg = f'Olá,{nome}! Seja bem-vindo(a)'
#     return msg
# mensagem = saudacao('yoriel')
# print(mensagem)
#--------------------------------------------------------------------------------------------------------------------------------
# def area(largura, comprimento):
#     area = largura * comprimento
#     return area
# largura = float(input('Digite a largura: '))
# comprimento = float(input('Digite a comprimento: '))
# print(area(largura, comprimento))
#--------------------------------------------------------------------------------------------------------------------------------
# def escreva(texto):
#     msg = texto.upper()
#     return msg
# text = str(input('Digite um texto: '))
# print(escreva(text))
# #--------------------------------------------------------------------------------------------------------------------------------
from random import randint

num = randint(0, 30)
print(num)