#declaração de variaveis
n: int = 0
soma: float = 1.0
cont: float = 0.0
fat: float = 1.0
#inicio
n = int(input('Digite um numero: '))
for cont in range (1, n + 1):
    fat = fat * cont
    soma = 1/fat
    print(f'A série é: {soma}')
#fim