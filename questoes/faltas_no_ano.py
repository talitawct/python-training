import math

obrigatoria = 75
aulas_semanas = 2
meses_de_aula = 4

presença = aulas_semanas * meses_de_aula * 4
faltas = (1 - obrigatoria / 100) * presença
faltas = round(faltas)

print(faltas)
