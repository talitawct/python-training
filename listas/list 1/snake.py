q1, q2, q3 = map(int, input().split())

e1, e2, e3 = map(int, input().split())

ovosEnve = e1+e2+e3
resultado = (q1+q2+q3) - ovosEnve - (ovosEnve * 2)

print(resultado)
