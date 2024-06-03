N = int(input())
forca_aprendizes = list(map(int, input().split()))
forca_yoda = int(input())

# identificando os Padawans selecionados
selecionados = [i for i, forca in enumerate(
    forca_aprendizes) if forca >= forca_yoda / 2]

# impressão dos identificadores dos Padawans selecionados
print(*selecionados)
