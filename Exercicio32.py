#definição de variaveis
fat: int = 1
i: int = 1
n: int = 0
#inicio
n = int(input('Digite um numero:'))
for i in range (1,n + 1):
    fat = fat * i
print(fat)
#fim