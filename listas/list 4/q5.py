N = int(input())
pontuacoes = list(map(int, input().split()))
cor_retira_pontos = int(input())

pontuacao_final = 0

# loop para calcular a pontuação final
for pontuacao in pontuacoes:
    if pontuacao == cor_retira_pontos:
        pontuacao_final -= pontuacao
    else:
        pontuacao_final += pontuacao

print(pontuacao_final)
