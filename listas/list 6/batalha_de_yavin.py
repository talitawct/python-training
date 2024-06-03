def batalha_de_yavin():
    N, M = map(int, input().split())
    espaco = [list(map(int, input().split())) for _ in range(N)]
    teleportes = [tuple(map(int, input().split())) for _ in range(M)]

    naves_destruidas = 0
    for teleport in teleportes:
        linha, coluna = teleport
        # luke atira para cima
        for i in range(linha-1, -1, -1):
            if espaco[i][coluna] == 1:
                naves_destruidas += 1
                espaco[i][coluna] = 0  # a nave foi destruída
                break
    return naves_destruidas


print(batalha_de_yavin())
