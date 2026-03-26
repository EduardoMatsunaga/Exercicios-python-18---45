ant: int = 0
pos: int = 1
fibo: int = 0
n: int = 0
cont: int = 1
#inicio
n = int(input('Digite um numero: '))
for cont in range (n): 
    fibo = ant + pos
    ant = pos
    pos = fibo
    print(fibo)
#fim