N = int(input())
alturas_obstaculos = list(map(int, input().split()))
habilidade_salto = int(input())

pulos = 0
venceu = 1

for altura in alturas_obstaculos:
    if altura > habilidade_salto:
        venceu = 0
        break
    pulos += 1

print(pulos)
print(venceu)
