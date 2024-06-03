def calcula_colheita(matriz, linha_harry, coluna_ron):

    peso_harry = sum(matriz[linha_harry])
    peso_ron = sum(matriz[i][coluna_ron] for i in range(len(matriz)))

    # Verifica o ponto de interseção entre as duas linhas.
    if linha_harry <= coluna_ron:
        peso_harry -= matriz[linha_harry][coluna_ron]
    else:
        peso_ron -= matriz[linha_harry][coluna_ron]

    return peso_harry, peso_ron


# Lê a entrada.
N = int(input())
matriz = [list(map(int, input().split())) for _ in range(N)]
linha_harry, coluna_ron = map(int, input().split())

# Calcula a colheita de Harry e Ron.
colheita_harry, colheita_ron = calcula_colheita(
    matriz, linha_harry, coluna_ron)

# Imprime a saída.
print("Harry", colheita_harry)
print("Ron", colheita_ron)

