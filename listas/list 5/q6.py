n = int(input())

# lê a quantidade de assassinatos de cada jogador
assassinatos = list(map(int, input().split()))

# lista de contadores para cada quantidade possível de assassinatos
contador_assassinatos = [0] * (max(assassinatos) + 1)

# contando a quantidade de jogadores para cada quantidade de assassinatos
for a in assassinatos:
    contador_assassinatos[a] += 1

# imprimindo a quantidade de assassinatos de cada jogador em ordem crescente
for i in range(len(contador_assassinatos)):
    print(f"{i} " * contador_assassinatos[i], end="")
