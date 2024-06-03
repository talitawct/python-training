segundos = int(input())

horas = int((segundos / 60) / 60)
min = int(segundos / 60 - (horas*60))
segundos = int(segundos - (((horas*60) + min)) * 60)

print(f"{horas}h {min}m {segundos}s")
