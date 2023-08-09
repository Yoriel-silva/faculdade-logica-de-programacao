ct = 0
total = 0
print('Digite -1 para sair')
while True:
    num = int(input('Digite um valor: '))
    if num == -1:
        break
    ct = ct + 1
    total = total + num
print(f'Foi digitado {ct} numeros')
print(f'O total dos numeros diitados foi {total}')

#usando a função while para soma de numeros