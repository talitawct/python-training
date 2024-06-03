XP_necessario = int(input())
quantidade_missoes = int(input())
XP_missoes = list(map(int, input().split()))
bonus_missoes = list(map(int, input().split()))

# Cálculo do total de XP obtido considerando os bônus
total_XP = sum(xp * bonus for xp, bonus in zip(XP_missoes, bonus_missoes))

if total_XP >= XP_necessario:
    print("Upou de Nivel!")
else:
    print("Nao foi dessa vez!")
