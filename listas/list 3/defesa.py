def verificar_resistencia(D, E, danos):
    for dia, dano in enumerate(danos, start=1):
        E -= dano
        if E <= 0:
            return dia
    return "Resistiu"


D, E = map(int, input().split())
danos = [int(input()) for _ in range(D)]

resultado = verificar_resistencia(D, E, danos)
print(resultado)
