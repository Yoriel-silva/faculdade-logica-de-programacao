print('digite -1 para sair')
ct = 0
total = 0
est = 1
while True:
    aluno = input(f'Digite a nota do aluno {est}:')
    if int(aluno) == -1:
        break
    ct = ct + 1
    total = total + int(aluno)
    est = est + 1
if ct == 0:
    print('Não pode ser divido por 0')
else:
    media = total / ct
    print(f'Essa turma tem {ct} alunos, e a media da turma foi {media:.2}')
    print(f'A soma das notas doas alunos foi {total}')
