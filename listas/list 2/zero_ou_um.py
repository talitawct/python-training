a, b, c = map(int, input().split())
if (0 <= a <= 1) and (0 <= b <= 1) and (0 <= c <= 1):
    if a != b and a != c:
        print("A")
    elif b != a and b != c:
        print("B")
    elif c != a and c != b:
        print("C")
    else:
        print("Empate")
