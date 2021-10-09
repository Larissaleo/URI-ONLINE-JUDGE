salario = float(input())

if salario <= 400:
    percentual=salario*0.15
    salarioNovo=salario+percentual
    print("Novo salario: %0.2f"%salarioNovo)
    print("Reajuste ganho: %0.2f"%percentual)
    print("Em percentual: 15 %")

elif salario > 400 and salario <=800:
    percentual=salario*0.12
    salarioNovo=salario+percentual
    print("Novo salario: %0.2f"%salarioNovo)
    print("Reajuste ganho: %0.2f"%percentual)
    print("Em percentual: 12 %")

elif salario >800 and salario <= 1200:
    percentual=salario*0.10
    salarioNovo=salario+percentual
    print("Novo salario: %0.2f"%salarioNovo)
    print("Reajuste ganho: %0.2f"%percentual)
    print("Em percentual: 10 %")

elif salario > 1200 and salario <=2000:
    percentual=salario*0.07
    salarioNovo=salario+percentual
    print("Novo salario: %0.2f"%salarioNovo)
    print("Reajuste ganho: %0.2f"%percentual)
    print("Em percentual: 7 %")

else:
    percentual=salario*0.04
    salarioNovo=salario+percentual
    print("Novo salario: %0.2f"%salarioNovo)
    print("Reajuste ganho: %0.2f"%percentual)
    print("Em percentual: 4 %")
    
    
    
