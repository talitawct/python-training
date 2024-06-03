N = int(input())
fases = list(map(int, input().split()))
M = int(input())

vida = M

for fase in fases:
    if fase == 1:
        vida = M
    elif fase >= 2:
        vida -= fase
        if vida <= 0:
            print("You Died")
            break

else:
    print("Yes, you can")
