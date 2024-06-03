inventario = []

# lendo dos itens do inventário
while True:
    item = input()
    if item == "fim":
        break
    inventario.append(item)

item_verificar = input()

# verificando se o item está no inventário
if item_verificar in inventario:
    print("item encontrado")
else:
    print("voce ainda nao descobriu este item")
