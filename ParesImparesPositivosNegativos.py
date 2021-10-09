cont = 0
par =0
impar =0
positivo=0
negativo=0
while cont < 5:
    num=int(input())
    cont=cont+1
    if num % 2 ==0:
     par=par+1
    else:
         impar=impar+1
    if num > 0:
            positivo=positivo+ 1
    elif num < 0:
            negativo=negativo+1
            
print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(positivo,"valor(es) positivo(s)" )
print(negativo,"valor(es) negativo(s)" )
    
