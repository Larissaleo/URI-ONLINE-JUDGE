nome = str(input())
salario = float(input())
vendas = float(input())

comissao = vendas*0.15
SalarioComBonus = comissao+salario

print("TOTAL = R$ %0.2f"%SalarioComBonus)
