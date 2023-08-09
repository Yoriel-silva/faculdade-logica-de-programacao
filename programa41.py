rodar = 1
windows = 0
unix = 0
Linux = 0
Netware = 0
Mac = 0
outro = 0
while rodar != 0:
    rodar = int(input('Qual o melhor sistema operacional para uso em servidores. 1-Windows Server. 2-Unix. 3-Linux. 4-Netware. 5-Mac OS. 6-Outro. 0-parar: '))
    if rodar == 1:
        windows = windows + 1
    elif rodar == 2:
        unix = unix + 1
    elif rodar == 3:
        Linux = Linux + 1
    elif rodar == 4:
        Netware = Netware + 1
    elif rodar == 5:
        Mac = Mac + 1
    elif rodar == 6:
        outro = outro + 1
    elif rodar == 0:
        rodar = 0
    else:
        print('Esse valora não é valido')
total = windows + unix + Linux + Netware + Mac + outro
if total == 0:
    print('Nenhum dado foi adicionado')
else:
    por_windows = windows / total * 100
    por_unix = unix / total * 100
    por_linux = Linux / total * 100
    por_netware = Netware / total * 100
    por_mac = Mac / total * 100
    por_outro = outro / total * 100

    print(f'{por_windows}% de usuarios usam windows')
    print(f'{por_unix}% de usuarios usam unix')
    print(f'{por_linux}% de usuarios usam linux')
    print(f'{por_netware}% de usuarios usam netware')
    print(f'{por_mac}% de usuarios usam mac')
    print(f'{por_outro}% de usuarios usam outro')