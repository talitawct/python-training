N = int(input())
habilidades = list(map(int, input().split()))
identificadores = list(map(int, input().split()))
elemento_escolhido = int(input())

# Identificação dos dobradores do elemento escolhido
dobradores_elemento = [identificador for habilidade, identificador in zip(
    habilidades, identificadores) if habilidade == elemento_escolhido]

if dobradores_elemento:
    print(*dobradores_elemento)
else:
    print("Nenhum")
