#declaração de variaveis
maria: float = 1.5
ana: float = 1.1
anos: int = 0
#inicio
while ana < maria:
    ana += 0.03
    maria += 0.02
    anos += 1
print(f'Serão necessários {anos} anos para Ana ser maior que Maria')
#fim