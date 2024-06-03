N = int(input())
itens = list(map(int, input().split()))

# inicialização da pilha para armazenar os itens da mochila
mochila = []

# inserção dos itens na pilha na ordem inversa
for item in reversed(itens):
    mochila.append(item)

# impressão dos itens retirados da mochila
print(*mochila)
