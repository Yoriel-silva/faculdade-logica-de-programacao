import math
a = int(input('Digite o valor de a: ')) 
if a == 0: 
    print('Não posso dividir por zero')
else:
    b = int(input('Digite o valor de b: ')) 
    c = int(input('Digite o valor de c: ')) 
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('Não existem raizes iguais')
    elif delta == 0:
        print('Existem dua raizes reais iguais')
        x1 = (-b + math.sqrt(delta)) / (2*a)
        print(f'O valor das raizes é {x1}')
    else: 
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'O valor da raiz x1 é {x1} e o valor da raiz x2 é {x2}')