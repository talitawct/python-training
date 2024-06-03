N, Q = map(int, input().split())


if N <= Q and (Q - N) % 2 == 0:
    print("vendido")
else:
    print("sinto muito")
