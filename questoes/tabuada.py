lista = "1 2 3 4 5 6 7 8 9 10 "
tabuada = list(map(lambda x: int(x) * 13, lista.split()))

print(tabuada)
  
#ou tabuada usando for i in range:#

numero = 13 # Nomeia variável e atribui o valor 13 a ele#

for i in range(1, 11):  # Loop de 1 a 10 sendo i variavel de interação
    #range funçã usada para gerar sequência de números
    # Sendo (1,11) partida e parada    
    resultado = numero * i # cria variável com nome de resultado e atribui o resultado da multiplicação a ela.
    print(f"{numero} x {i} = {resultado}")