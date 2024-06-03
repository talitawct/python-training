time = 3
min = 23
seconds = 17
# Acima nomeio 3 variáveis e atribuo valores a elas
time_convert = (time * 3600) + (min * 60) + seconds
# Aqui crio uma variável e atribuo a ela o valor das somas de (time * 3600) sendo 3600 a quantidade de segundos em 1 hora,
# em seguida (min * 60) que é a quantidade de segundos por minuto + 17 segundos
print(f"{time} horas, {min} minutos e {seconds} segundos são equivalentes a {time_convert} segundos.")
