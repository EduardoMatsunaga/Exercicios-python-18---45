#definição de variaveis
soma: int = 0
n: int = 0
cont: int  = 0
#inicio
for cont in range (1,16):
    n = cont / (cont * cont)
    if cont  % 2 == 0:
        soma = soma - n
        print(f'-{cont}/{cont*cont} = ', n)
    else: 
        soma = soma + n
        print(f'+{cont}/{cont * cont} = ', n) 
#fim