#definição de variaveis
casa: int = 64
graos: int = 1
cont: int = 0
#inicio
for cont in range(1,65):
    casa += graos
    graos *= 2
print(f'A quantidade de graos é: {graos} ')
#fim