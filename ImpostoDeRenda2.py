salario = float(input())

if salario <= 2000.00:
    i = 0
    print('Isento')
    
if 2000.00 < salario <= 3000.00:
    r8 = salario - 2000.00
    i = r8 * (8 / 100)
    
if 3000.00 < salario <= 4500.00:
    i8 = (8 / 100) * (1000.00)
    r18 = salario - 3000.00
    i = r18 * (18 / 100) + i8
    
if salario > 4500.00:
    i8 = (8 / 100) * (1000.00)
    i18 = (18 / 100) * (1500.00)
    r28 = salario - 4500.00
    i = i18 + i8 + r28 * (28 / 100)

if salario > 2000.00:
    i = float(i)
    print("R$ %0.2f"%i)
    
