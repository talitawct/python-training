tabuleiro = [list(map(int, input().split())) for _ in range(8)]
X, Y = map(int, input().split())

# contagem de peças inimigas
contagem = 0

# verificando as peças na mesma linha à direita da torre
for i in range(Y+1, 8):
    if tabuleiro[X][i] == 2:
        contagem += 1
        break
    elif tabuleiro[X][i] == 1:
        break

# verificando as peças na mesma linha à esquerda da torre
for i in range(Y-1, -1, -1):
    if tabuleiro[X][i] == 2:
        contagem += 1
        break
    elif tabuleiro[X][i] == 1:
        break

# verificando as peças na mesma coluna acima da torre
for i in range(X-1, -1, -1):
    if tabuleiro[i][Y] == 2:
        contagem += 1
        break
    elif tabuleiro[i][Y] == 1:
        break

# verificando as peças na mesma coluna abaixo da torre
for i in range(X+1, 8):
    if tabuleiro[i][Y] == 2:
        contagem += 1
        break
    elif tabuleiro[i][Y] == 1:
        break

print(contagem)
