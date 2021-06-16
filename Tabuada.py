print('Bem Vindo!!! Esta tabuada realiza operações apenas com os 20 primeiros números.') 
n = int(input('Insira um número de entre 1 e 100:   '))
if n > 100:
    print('Operação Inválida')

    exit('Operação Inválida')
    
t = input('Escolha entre E - EXPONENCIAL, M - MULTIPLICAÇÃO, S - SOMA :    ')
if t == "M" and n < 101:
    s = 1
    print(n)
    while s < 21:
         v = n*s
         s = s+1
         print (v)
    
elif t == 'S' and n < 101:
    s = 1
    while s < 21:
        v = n + s
        s = s+1
        print (v)
    
elif t == 'E' and n < 101:
    s = 1
    while s < 21 :
        v = n ** s
        s = s + 1
        print (v)


