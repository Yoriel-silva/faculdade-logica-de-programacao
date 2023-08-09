'''Exercicio 1
import math
base = float(input('Digite o valor da base do cilindro: '))
r = float(input('Digite o valor do raio: '))
area = 2 * math.pi * r * base
print(f'A área lateral do cilindro é {area}')'''

'''Exercicio 2
v1 = int(input('Digite o valor 1: '))
v2 = int(input('Digite o valor 2: '))
if v1 > v2:
    print(f'{v2},{v1}')
elif v2 > v1:
    print(f'{v1},{v2}')
else:
    print(f'{v1}={v2}')'''

''' Exericio 3
ct = 0
soma = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    ct = ct + 1
    soma = soma + valor
media = soma / ct
print(f'A quantidade de valores informatos foi {ct}')
print(f'A soma dos numeros digitados foi {soma}')
print(f'A media aritimetica foi {media}')'''