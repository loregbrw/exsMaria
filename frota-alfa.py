ano_luz = {
"pc": 0.31,
"al": 1,
"ae": 63241.09,
"ml": 525960.23,
"sl": 31557609.92
}

unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]

opcao = 1

for i in unidades:
    print(i)

valor = float(input("\nValor a ser convertido: "))
unidade_origem = input("Converter de: ")
unidade_destino = input("Converter para: ")

if unidade_destino in ano_luz and unidade_origem in ano_luz:
    conversao = valor / ano_luz[unidade_origem]
    conversao = conversao * ano_luz[unidade_destino]

    print(f"Conversão: {valor} {unidade_origem} = {conversao} {unidade_destino}")

