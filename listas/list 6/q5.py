N = int(input())
mapa = [list(map(int, input().split())) for _ in range(N)]
C = int(input())

total_especies = 0

# loop para verificar as coordenadas e somar as espécies
for _ in range(C):
    x, y = map(int, input().split())
    total_especies += mapa[x][y]

print(total_especies)
