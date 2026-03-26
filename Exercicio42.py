#definição de variaveis
deno: int = 0
cont: int = 1
soma: float  = 0.0
#inicio
while cont < 51:
    deno = cont / (2*cont + 1)
    cont += 1
    soma += deno
print(soma)
#fim