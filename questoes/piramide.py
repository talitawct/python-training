'''a = '*'
b = 15

i =  1 

while i <= b: 
        print (a * i)
        i += 1
        if i > 5:
            break'''

a = '*'
b = 15

for i in range(1, b+1):
    print(a*i)
    if i == 5:
        break
