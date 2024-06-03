N, T = map(int, input().split())

# verificando os títulos dos livros
for _ in range(N):
    titulo = input()
    qtd_consoantes = sum(
        1 for char in titulo if char in "bcdfghjklmnpqrstvwxyz")

    if qtd_consoantes > T:
        print(0)
    else:
        print(1)
