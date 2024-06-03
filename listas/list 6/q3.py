def corrigir_mapa(mapa):

    def posicao_valida(i, j):
        return 0 <= i < 10 and 0 <= j < 10

    def verifica_contato_terra(i, j):
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if posicao_valida(ni, nj) and mapa[ni][nj] == '*':
                return True
        return False

    for i in range(10):
        for j in range(10):
            if mapa[i][j] == 't' and verifica_contato_terra(i, j):
                mapa[i][j] = 'p'

    return mapa


mapa = [input().split() for _ in range(10)]

mapa_corrigido = corrigir_mapa(mapa)


for linha in mapa_corrigido:
    print(' '.join(linha))
