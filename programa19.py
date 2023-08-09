ct = 0
total = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 0:
        break
    par = num % 2
    if par == 1:
        print('esse numero é impar')
    else: 
        total = total + num
        ct = ct + 1
if ct == 0:
    print('Não é divisivel por 0')
else:
    media = total / ct
    print(f'O total da soma dos numeros pares foi {total}')
    print(f'A media é {media}')