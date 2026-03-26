#declaração de variaveis
result: int = 0
a: int = 0
b: int = 0
#inicio
a = int(input('Digite um valor:'))
b = int(input('Digite um valor:'))
if a > b:
    result = a - b
else:
    result = b - a
print('A diferença do maior pelo menor:', result)
#fim