n1, n2, n3, n4, n5, n6 = map(int, input().split())

pont_total = n1 + n2 + n3 + n4 + n5 + n6

if pont_total >= 250:
    nota = "S+"
elif pont_total >= 200:
    nota = "S"
elif pont_total >= 180:
    nota = "S-"
elif pont_total >= 150:
    nota = "A+"
elif pont_total >= 100:
    nota = "A"
elif pont_total >= 80:
    nota = "A-"
elif pont_total >= 60:
    nota = "B+"
elif pont_total >= 40:
    nota = "B"
else:
    nota = "B-"

print(nota)
