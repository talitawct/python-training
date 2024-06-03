def imprimir_piramide(P):
    for i in range(1, P + 1):
        espacos = ">" * (P - i)
        blocos = "#" * i
        linha = espacos + blocos
        print(linha)


P = int(input())

imprimir_piramide(P)
