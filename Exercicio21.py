#definição de  variaveis
media: float  = 0.0
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
#inicio
n1 = float(input('Digite a sua nota:'))
n2 = float(input('Digite a sua nota:'))
n3 = float(input('Digite a sua nota:'))
n4 = float(input('Digite a sua nota:'))
media = (n1 + n2 + n3 + n4) / 4
if media >= 6.0:
    print('Aprovado')
elif media >= 3.0 and media < 6.0:
    print('Exame')
else:
    print('Retido')
#fim