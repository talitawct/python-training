def verificar_ocorrencias(frase, qtd_ocorrencias, palavra):
    # Remove espaços em branco e converte para minúsculas
    frase = frase.replace(" ", "").lower()
    palavra = palavra.lower()

    # Conta as ocorrências da palavra na frase
    ocorrencias = frase.count(palavra)

    # Imprime a quantidade de ocorrências
    print(ocorrencias)

    # Verifica se a quantidade de ocorrências é igual a qtd_ocorrencias
    if ocorrencias == qtd_ocorrencias:
        print("SIM!")
    else:
        print("NAO!")

# Entrada
frase = input()
qtd_ocorrencias, palavra = input().split()
qtd_ocorrencias = int(qtd_ocorrencias)

# Chama a função
verificar_ocorrencias(frase, qtd_ocorrencias, palavra)
