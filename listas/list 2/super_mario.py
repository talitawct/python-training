SC, MM, CK = map(int, input().split())

if SC == 30:
    print("PROXIMO MUNDO")
else:
   
    faltando_SC = 30 - SC
    faltando_MM = 6 - MM
    faltando_CK = 3 - CK


    print(f"{faltando_SC} {faltando_MM} {faltando_CK}")