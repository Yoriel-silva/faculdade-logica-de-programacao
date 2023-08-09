ano = int(input('Digite o ano de seu nascimento: '))
idade = 2023 - ano
print(f'Você tem {idade} anos')
if idade >= 16:
    print('Você pode votar')
else:
    print('Você não pode votar')