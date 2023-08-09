def max(v1,v2):
    if v1 > v2:
        max = v1
    else:
        max = v2
    return max

if __name__ == '__main__':
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite um valor: '))
    print(max(v1,v2))