n1 = int(input('Digite um numero inteiro: '))

resto = n1 % 2

if resto == 0:
    print(f'{n1} é um numero par')
else:
    print(f'{n1} é um numero impar')
print(f'O valor digitado foi {n1}')
print(f'O valor do resto é {resto}')