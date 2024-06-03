N = int(input())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
D = list(map(int, input().split()))

# verificando se o Dr. Strange consegue viajar para D
ok = all(ui + vi == Di for ui, vi, Di in zip(u, v, D))

print("OK" if ok else "NOPE :(")
