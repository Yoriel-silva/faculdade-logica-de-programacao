menor_valor = 999999999
maior_valor = -99999999
ct = 0
soma = 0
print('Digite [0] para sair')
while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    ct = ct + 1
    soma = soma + valor
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
if ct == 0:
    print('Nenhum valor foi digitado')
else:
    print(f'O menor valor digitado foi {menor_valor}')
    print(f'O menor valor digitado foi {maior_valor}')
    print(f'A quantidade de numeros digitados foi {ct}')
    print(f'A soma dos numeros digitados foi {soma}')