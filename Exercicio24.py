#declaração de variaveis
x: int = 0
#inicio
x = int(input('Digite um valor inteiro:'))
if (x % 2 == 0) and (x % 3 == 0):
    print('É divisivel por 2 e 3')
else:
    print('Não é divisivel por 2 e 3')
#fim
