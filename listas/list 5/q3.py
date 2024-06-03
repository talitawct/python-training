palavra = input()

# verificando se é um palíndromo
if palavra == palavra[::-1]:
    print("Sim")
else:
    print("Nao")
