def proteger_vila(N, C, ondas):
    clones_na_vila = C

    for onda in ondas:
        quantidade_zetsus, quantidade_clones = onda
        clones_na_vila += quantidade_clones

        if quantidade_zetsus > clones_na_vila:
            return "Madara venceu"

        clones_na_vila -= quantidade_zetsus

    return "Naruto defendeu a Vila"


N, C = map(int, input().split())
ondas = [list(map(int, input().split())) for _ in range(N)]

resultado = proteger_vila(N, C, ondas)
print(resultado)
