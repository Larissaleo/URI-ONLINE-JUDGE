n =int(input())
cont =0
In = 0
Out = 0
while cont < n:
    x = int(input())
    cont=cont+1
    if x >=10 and x <=20:
        In=In+1
    else:
        Out=Out+1
print(In,"in")
print(Out,"out")
