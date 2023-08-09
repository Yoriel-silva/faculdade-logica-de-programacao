genero = int(input('Qual seu genero?\nhomem[0]\nmulher[1]\n'))
altura = float(input('Qual sua altura: '))

if genero == 0:
    peso = 72.7 * altura - 58
    print(f'Seu peso ideal é {peso}')
else:
    peso = 62.1 * altura - 44.7
    print(f'Seu peso ideal é {peso}')