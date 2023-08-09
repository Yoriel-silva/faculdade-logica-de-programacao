ct =0
soma = 0
n1 = int(input('Digite o numero inicial: '))
n2 = int(input('Digite o numero final: '))
cd = int(input('Será decrescente[-1] ou crescente[1]: '))
if n2 > n1:
    x = 1
    print('crescente:')
elif n1 > n2:
    print('decrescente:')
    x = -1
else:
    print('os valores são iguais')
    x = 1
for n in range(n1, n2+x, cd):
    print(n)
    ct = ct + 1
    soma += n
print(ct)
print(soma)