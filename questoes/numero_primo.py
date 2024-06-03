n1 = int(input("Digite um número: "))

if n1 <= 1:
    print("Não é um número primo")
else:
    for i in range(2, n1):
        if n1 % i == 0:
            print("Não é um número primo")
            break
    else:
        print(n1, "É um número primo")
