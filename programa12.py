n1 = int(input('Digite um numero: '))

if n1 > 0:
    print(f'{n1} é positivo')
    print('o dobro é ', n1 * 2)
elif n1 == 0:
    print(f'{n1} nulo')
else:
    print(f'{n1} é negativo')
    print('o triplo é ', n1 * 3)
print(f'O numero digitado foi {n1}')