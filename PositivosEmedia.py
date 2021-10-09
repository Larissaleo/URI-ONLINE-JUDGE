cont =0
SomaPositivo = 0
media=0

while cont < 6:
    num =float(input())
    cont=cont+1
    if num > 0:
        SomaPositivo=SomaPositivo+1
        media=media + num
print(SomaPositivo, "valores positivos")
print("%0.1f"%(media/SomaPositivo))
    
