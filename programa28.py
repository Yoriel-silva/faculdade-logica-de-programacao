ct = soma = 0
for n in range(1, 3+1):
    nota = float(input('Digite a nota: '))
    ct = ct + 1
    soma = soma + nota
if ct == 0:
    print('Deve ser digitado pelo menos uma nota')
else:
    media = soma/ct
    print(media)

# calculando media aritimetica usando for