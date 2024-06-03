a, b, c = map(int, input().split())
if (100 <= a <= 200) and (100 <= b <= 200) and (100 <= c <= 200):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)




