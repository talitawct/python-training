def pode_invocar_naruto(ninjas):
    while ninjas > 1 and ninjas % 2 == 0:
        ninjas //= 2

    return "Dattebayo" if ninjas == 1 else "Tururuuu"


N = int(input())

resultado = pode_invocar_naruto(N)
print(resultado)
