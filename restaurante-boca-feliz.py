estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}

cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

pedido = {1: "x-burguer", 2: "x-salada", 3: "x-bacon", 4: "x-egg", 5: "x-tudo"}

op = 1

for food, ingredients in cardapio.items():
     print(f"{op}. {food}: {ingredients}")
     op += 1

while op != 0:
    op = int(input("O que deseja pedir (0 para sair)?"))
    if op < 1 or op > 5:
         print("Item não localizado no cardápio")
    else:
         for i in cardapio.get(pedido[op]):
         