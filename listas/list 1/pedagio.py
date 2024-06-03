t, d = map(int, input().split())

v, p = map(int, input().split())

qt_pedagio = int(t/d)
total_por_km = int(v*t)
total_por_pedag = int(p*qt_pedagio)

resultado = int(total_por_km + total_por_pedag)
print(resultado)
