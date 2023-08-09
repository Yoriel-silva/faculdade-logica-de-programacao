n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(f'A media é {media:.2},', end = ' ')

if media >= 5:
    print('Aluno aprovado')
else:
    print('aluno reprovado')

#feito