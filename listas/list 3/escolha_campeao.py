n = int(input())

lista = [None] * n
'''
lista2 = [n]
lista2 = [1,2,3,4]

'''
# print("Tamanho da lista: ", lista)
for i in range(0, n):
    lista[i] = int(input())

# print("Tamanho da lista: ", lista)
auxiliar = lista[0]

for i in range(0, n-1):
    if auxiliar > lista[i + 1]:
        continue  # break
    else:
        auxiliar = lista[i+1]

print(auxiliar)
