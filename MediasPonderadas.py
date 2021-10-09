n =int(input())
cont =0
media=0
while cont < n:
    cont=cont+1
    lista =list(map(float,input().split()))
    x1,x2,x3 = lista
    x1 = x1*2
    x2 = x2*3
    x3 = x3*5
    media=(x1+x2+x3)/10

print("%0.1f"%media)
