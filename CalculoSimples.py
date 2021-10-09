CodigoPeca1 = int(input())
QtdPeca1 = int(input())
ValorPeca1 =float(input())
CodigoPeca2 = int(input())
QtdPeca2 = int(input())
ValorPeca2 =float(input())

TotalPeca1 = QtdPeca1*ValorPeca1
TotalPeca2 = QtdPeca2*ValorPeca2

total = TotalPeca1+TotalPeca2

print("VALOR A PAGAR: R$ %0.2F"%total)
