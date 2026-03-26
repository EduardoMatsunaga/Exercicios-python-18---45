#declaração de variaveis
a: int = 0
b: int = 0
c: int = 0
d: int = 0
#inicio
a = int(input('Digite um valor (menor):'))
b = int(input('Digite um valor (maior que o primeiro):'))
c = int(input('Digite um valor (maior que o segundo):'))
d = int(input('Digite um valor (aleatorio):'))
if a > d:
   print(f'A ordem é: {d}, {a}, {b}, {c}.')
elif b > d:
   print(f'A ordem é: {a}, {d}, {b}, {c}.')
elif c > d:
   print(f'A ordem é: {a}, {b}, {d}, {c}.')
else:
   print(f'A ordem é: {a}, {b}, {c}, {d}.')
#fim