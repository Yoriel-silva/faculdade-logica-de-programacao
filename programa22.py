maior_altura = 0
menor_altura = 10
ct_masc = 0
ct_fem = 0
soma = 0
print('Digite [-1] para sair')
while True:
    altura = float(input('Qual a sua altura: '))
    if altura == -1:
        break
    genero = input('Qual o seu genero [F - feminino, M - masculino]: ')
    soma = soma + altura
    if genero == 'M':
        ct_masc = ct_masc + 1
    else:
        ct_fem = ct_fem + 1
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
media = soma / (ct_masc + ct_fem)
print(f'A maior altura foi {maior_altura}')
print(f'A menor altura foi {menor_altura}')
print(f'A quantidade de homens foi {ct_masc}')
print(f'A quantidade de mulheres foi {ct_fem}')
print(f'A media é {media:.2f}')
