def calcular_total_bolinhas(N, Q):
    total = Q

    for _ in range(2, N + 1):
        Q *= 2
        total += Q

    return total


N, Q = map(int, input().split())

resultado = calcular_total_bolinhas(N, Q)
print(resultado)
