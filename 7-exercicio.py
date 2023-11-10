def valorPagamento(valor, dias):
    if dias > 0:
        valor = valor + (valor * 0.03)
        for i in range(dias):
            valor = valor +  (valor * 0.001)
    return valor

op = 5
prestacoes = []

def valorTotal(lista, valor_total):
    valor_total = 0
    for i in lista:
        valor_total += i

    return valor_total

while (op != 0):

    valor = float(input("DIgite o valor da prestação: "))
    dias = int(input("Digite a quantidade de dias em atraso: "))

    pagamento = valorPagamento(valor, dias)

    print(pagamento)
    prestacoes.append(pagamento)

    op = int(input("Digite 0 para sair: "))

print(f"Quantidades de presações hoje: {len(prestacoes)}, valor total: R${valorTotal(prestacoes, 0)}")