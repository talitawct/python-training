s = input()
invertida = ""

'''Duas variáveis uma com a função de receber a entrada de dados
A segunda é uma variável auxiliar, uma string vazia'''

for c in s:
    # O for vai percorrer o loop com a variável 'c' de caractere
    # Para cada elemento da string 's'
    invertida = c + invertida
''' Aqui atribuo a variável auxiliar 'invertida' a concatenação de cada
elemento que o for percorrer, colocando à esquerda da string '''
print(invertida)
