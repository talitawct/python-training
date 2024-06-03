def calcular_soma_ataque_defesa(jogadores, soldados_por_jogador, informacoes_soldados):
    for i in range(jogadores):
        soma_ataque = 0
        soma_defesa = 0

        for j in range(soldados_por_jogador):
            ataque, defesa = map(int, input().split())
            soma_ataque += ataque
            soma_defesa += defesa

        print(soma_ataque, soma_defesa)


jogadores = int(input())
soldados_por_jogador = int(input())

calcular_soma_ataque_defesa(jogadores, soldados_por_jogador, None)
