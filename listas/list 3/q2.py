n = int(input())

lista = [None] * n

for i in range(0, n):
    lista[i] = int(input())

auxiliar = lista[0]

for i in range(0, n-1):
    if auxiliar > lista[i + 1]:
        continue
    else:
        auxiliar = lista[i+1]

print(auxiliar)
