x_cordenada, y_cordenada = map(int, input().split())
x_drone, y_drone = map(int, input().split())
if x_cordenada == x_drone and y_cordenada == y_drone:
    print("Soltar pacote")
else:
    print("Nao soltar pacote")
