n = 1243

''' calculo cada elemento do numero acima,
decompondo ele apartir do sistema de numeração,
utilizando % para pegar o resto da divisão'''

m = n // 1000
c = (n % 1000) // 100
d = (n % 100) // 10
u = n % 10

''' Crio uma variável para receber o resultado do calculo acima,
em seguida transformo em uma lista'''
n_2 = [m, c, d, u]

''' outra variável utilizando a função 'len', que retorna
o comprimento do objeto, no caso dessa variável, o objeto é a lista,
ou seja, 'troca' tem o comprimento de 'n_2'''
troca = len(n_2)

''' utilizo o looping 'for' para iterar sobre metade dos elementos 
dentro da variável'''
for i in range(troca // 2):
    n_2[i], n_2[troca - i - 1] = n_2[troca - i - 1], n_2[i]

''' Aqui o bagulho é doido, uso a simetria de Einstein entre as duas variáveis,
uma espelhando a outra, n_2 se refere ao elemento no indice 'i', o valor de n_2[i] é substituido
pelo valor original em n_2[troca -i -1] do outro lado acontece o mesmo invertendo a ordem
 '''
print(n_2)


'''n = 1243

m = n // n
c = (n % 1000) // 100
d = (n % 100) // 10
u = n % 10

troca = (u * 1000) + (d * 100) + (c * 10) + (m * 1)
# troca = int(''.join(map(str, [u, d, c, m])))

print(troca)
'''
