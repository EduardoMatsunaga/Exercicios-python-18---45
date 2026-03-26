n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 < n2:
    menor = n1
    maior = n2
else:
    menor = n2
    maior = n1

for num in range(menor + 1, maior):
    if num > 1:
        primo = True

        for i in range(2, num):
            if num % i == 0:
                primo = False
                break

        if primo:
            print(num)
#fim