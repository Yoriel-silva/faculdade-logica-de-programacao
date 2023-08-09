print('Tabuada de multiplicação:') #show on the screen
ct = 0 #create a counter
while True: #start a loop
    num = int(input('Digite um numero, [-1 para sair]: ')) #ask a information to the user
    if num == -1: # create a condition
        break # break the loop
    for n in range(1,10+1): # create a loop, with a determined range
        print(f'{n} * {num} = {num * n}') #show on the screen
        # print('{:2} X{:2} = {:2}'.format(n, num, (n*num)))
    ct = ct + 1 #add +1 to the counter each time the loop run
print(f'O programa rodou {ct} vezes') #show on the screen