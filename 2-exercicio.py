def imprimirValorN(n):
    for i in range(n):
        print(i + 1, end=" ")
    print("\n")

n = int(input("Digite um número: "))

for i in range(n + 1):
    imprimirValorN(i)