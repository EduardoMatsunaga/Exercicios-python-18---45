#definição de variaveis
n: int = 0
i: int = 0
mult: int = 0
#inicio
n = int(input('Digite um numero:'))
for i in range (1, 11):
    mult = n * i
    print(n, 'x', i, '=', mult)
#fim
