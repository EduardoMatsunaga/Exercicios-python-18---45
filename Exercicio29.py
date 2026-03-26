#declaração de variaveis
tipo: int = 0
valor: float = 0.0
corrigido: float  = 0.0
#inicio 
tipo = int(input('Digite o tipo de investimento (1 = poupança) (2 = renda fixa):'))
valor = float(input('Digite o valor do investimento:'))
if tipo == 1:
    corrigido = valor * 1.03
    print('Valor corrigido', corrigido)
elif tipo == 2:
    corrigido = valor * 1.05
    print('Valor corrigido', corrigido)
else:
    print('Invalido')
#fim