#declaração de variaveis
a: int = 0.0
b: int = 0.0
#inicio
a = int(input('Digite um valor:'))
b = int(input('Digite um valor:'))
if a > b:
    print('Valores em ordem crescente:', b , a)
else: 
    print('Valores em ordem crescente:', a , b)
#fim