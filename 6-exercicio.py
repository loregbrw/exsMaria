def converterHora(hora):
    if hora > 12:
        hora -= 12
        return (hora, "P.M.")
    return (hora, "A.M.")

def printar(hora, minuto):
    h, texto  = converterHora(hora)
    print(f"{h}:{minuto} {texto}")

while True:

    h = int(input("Digite a hora: "))
    m = int(input("Digite os minutos: "))

    printar(h, m)

    op = input("Deseja continuar? ")
    if op == "não":
        break