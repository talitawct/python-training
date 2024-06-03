def monitorar_vulcao(T, pressoes):
    for pressao in pressoes:
        if pressao > T:
            return "ALARME"
    return "O Havai pode dormir tranquilo"


T = int(input())
pressoes = []
pressao = int(input())
while pressao != 0:
    pressoes.append(pressao)
    pressao = int(input())

resultado = monitorar_vulcao(T, pressoes)
print(resultado)
