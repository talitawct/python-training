l1, p1 = map(int, input().split())
l2, p2 = map(int, input().split())
l3, p3 = map(int, input().split())

total_l = l1 + l2 + l3
total_p = p1 + p2 + p3

if total_l > total_p:
    print("Lucas")
elif total_p > total_l:
    print("Pedro")
else:
    print("Empate")
