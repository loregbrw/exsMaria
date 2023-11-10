def valor(a):
    if a > 0:
        return "P"
    else:
        return "N"
    
num = int(input("Digite um número: "))

print(valor(num))