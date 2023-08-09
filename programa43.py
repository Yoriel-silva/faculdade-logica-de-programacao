#Exercicio 1
'''import math
raio = float(input('Qual o raio da esfera? '))
volume = 4 * math.pi * raio**3 /3
print(f'O volume da esfera é {volume}')'''

#Exercicio 2
'''print('Digite [0] para sair')
ct_par = 0
soma_par = 0
ct_impar = 0
soma_impar = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    par = valor % 2
    if par == 0:
        ct_par = ct_par + 1
        soma_par = soma_par + valor
    else:
        ct_impar = ct_impar + 1
        soma_impar = soma_impar + valor
if ct_par == 0:
    print('Nenhum valor par foi digitado')
elif ct_impar == 0:
    print('Nenhum valor impar foi digitado')
else:
    media_par = soma_par / ct_par
    media_impar = soma_impar / ct_impar
    print(f'A media aritimetica dos numeros pares digitados é {media_par}')
    print(f'A media aritimetica dos numeros impares digitados é {media_impar}')'''