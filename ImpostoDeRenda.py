salario = float(input())
isento = 2000

if salario >= 0 and salario <=2000:
    print("Isento")

elif salario > 2000 and salario <=3000:
    salarioTaxa=salario-isento
    valorImposto=salarioTaxa*0.08
    print("R$ %0.2f"%ValorImposto)

elif salario > 3000 and salario <= 4500:
     salarioTaxa=salario-isento
     
