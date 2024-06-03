n = 8


if (n == 1):
    print(0)
elif (n == 2) or (n == 3):
    print(1)
else:
    a = 1
    b = 1
    for i in range(2, n):
        fibonacci = a + b
        a = b
        b = fibonacci

print(fibonacci)
