compra = float(input('Digite qual foi o valor da compra: '))
venda = float(input('Digite qual foi o valor da venda: '))
total = venda - compra

if total > 0:
    print('Você teve lucro')
elif total == 0:
    print('Os valores são iguais')
else:
    print('Você teve prejuizo')
print(f'O valor da compra foi {compra}')
print(f'O valor da venda foi {venda}')