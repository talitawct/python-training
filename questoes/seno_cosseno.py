hipotenusa = 13
c_oposto = 5
c_adjacente = 12
angulo = 80
'''nomeia as variáveis e atribuo valor a elas do tipo inteiro'''
sen_x = round(c_oposto / hipotenusa, 2)
coss_x = round(c_adjacente / hipotenusa, 2)
tangente = round(c_oposto / c_adjacente, 2)
secante = round(1/coss_x, 2)
co_secante = round(1 / sen_x, 2)
cotangente = round(1 / tangente, 2)
''' Aqui calculo os valores de seno, cosseno, tangente e por diante, 
usando a função round que arredonda um numero inteiro, ou numero especifico com casa decimais. 
E o "ndigits" representado pelo "2" é numero de casas decimais que escolhi manter'''
r_Trigonometrico = sen_x, coss_x, tangente, secante, co_secante, cotangente
'''variável auxiliar, onde atribuo o resultado dos calculos acima'''

# [float(f"{result:.2f}") for result in r_Trigonometrico]

'''Aqui percorro cada elemento da lista com "for result in r_Trigonometrica" 
atribuindo "r_Trigonometrica" a "result" temporariamente. Em seguida f"{result:.3f}"
para formatar o número "result" com três casas decimais, 2f infatiza as casa decimais. Depois converto tudo em float (ponto flutuante) '''
print(r_Trigonometrico)
