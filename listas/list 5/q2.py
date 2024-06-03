def abreviar_nome(nome_completo):
    partes_nome = nome_completo.split()
    abreviacoes = [parte[0].upper() + '.' for parte in partes_nome[:-1]]
    sobrenome = partes_nome[-1].capitalize()
    return ' '.join(abreviacoes) + ' ' + sobrenome


def main():
    n = int(input())
    autores = []

    for _ in range(n):
        nome_autor = input()
        autores.append(abreviar_nome(nome_autor))

    for autor_abreviado in autores:
        print(autor_abreviado)


if __name__ == "__main__":
    main()
