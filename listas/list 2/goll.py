N, Q = map(int, input().split())


if N <= Q and (Q - N) % 2 == 0:
    print("vendido")
else:
    print("sinto muito")



zagueiro, goleiro = input().split()
drible, chute = input().split()

if drible != zagueiro:
    print("Bloqueado")
else:
    print("Driblado")
    if chute != goleiro:
        print("...e o goleiro pega")
    else:
        print("Gol")