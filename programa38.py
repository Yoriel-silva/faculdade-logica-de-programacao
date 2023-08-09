def soma(v1,v2):
    return v1 + v2
def sub(v1,v2):
    return v1 - v2

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
op = int(input('Você qwuer somar[1] ou subtrair [2]: '))
if op ==1:
    print(soma(v1,v2))
else:
    print(sub(v1,v2))
