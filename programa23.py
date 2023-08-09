print('Números naturais na vertical: ')
n = 1
soma = 0
ct = 0
while n <= 13:
    r = n % 2
    if r != 0:
        print(n)
        ct = ct + 1
        soma = soma + n
    n = n + 1 
print(f'Foram mostrados {ct} numeros ')
print(f'A soma dos numeros é {soma}')