estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}

cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

pedido = {1: "x-burguer", 2: "x-salada", 3: "x-bacon", 4: "x-egg", 5: "x-tudo"}

opcao = 1

concluido = True

for hamburguers, ingredientes in cardapio.items():
     print(f"{opcao}. {hamburguers}: {ingredientes}")
     opcao += 1

while opcao != 0:
     opcao = int(input("O que deseja pedir (0 para sair)? "))
     if opcao >= 1 or opcao <= 5:
         concluido = True
         for i in cardapio.get(pedido[opcao]):
               if estoque[i] > 0:
                    estoque[i] -= 1
               else:
                    print(f"Infelizmente acabou o {i}")
                    concluido = False
     if concluido == True:
          print(f"um {pedido[opcao]} saindo no capricho!!!")

