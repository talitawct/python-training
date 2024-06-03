S, N = map(int, input().split())
pulos = [int(input()) for _ in range(S)]

pedras = [0] * N

for pulo in pulos:
    for i in range(0, N, pulo):
        pedras[i] = 1

print(' '.join(map(str, pedras)))
