#definição de variaveis
n: int = 0
maior: int = 0
menor: int = 0
cont: int = 0
#inicio
while cont < 100: 
    n = int(input('Digite um numero positivo: '))
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1 
print(f'O maior número é: {maior}')
print(f'O menor numero é: {menor}')
#fim