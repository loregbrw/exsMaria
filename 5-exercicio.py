def somaImposto(custo, taxa_imposto):
    taxa_imposto = taxa_imposto / 100 * custo
    custo = taxa_imposto + custo
    return custo

valor = float(input("Digite o custo: "))
taxa = int(input("Digite a porcentagem da taxa sobre o produto: "))

print(f"O valor com imposto é: R${somaImposto(valor, taxa)}")