n = int(input())

moedas = []

# Lê as moedas e as armazena na lista
for _ in range(n):
    cor, valor = input().split()
    valor = int(valor)
    moedas.append((cor, valor))

limite = int(input())

moedas_somadas = []

# soma as moedas com valor maior ou igual ao limite e as salva na lista
for cor, valor in moedas:
    if valor >= limite:
        moedas_somadas.append((cor, valor))

# imprime as moedas somadas
for cor, valor in moedas_somadas:
    print(f"{cor} {valor}")

# calcula e imprime o valor total das moedas
total = sum(valor for _, valor in moedas_somadas)
print(total if moedas_somadas else 0)
