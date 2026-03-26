#definição de variaveis
menor: int = 0
maior: int = 0
n1: int = 0 
n2: int = 0
cont: int = 0 
soma: int = 0
#inicio
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1 > n2:
    menor = n2
    maior = n1
else:
    maior = n2
    menor = n1 
for cont in range(menor +1 , maior):
    if cont % 2 != 0: 
        soma += cont
print(f'A somatoria dos numeros impares é: {soma}')
#fim