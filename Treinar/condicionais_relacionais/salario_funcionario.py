salario = float(input('Digite o seu salario: '))
if salario > 1250:
    novo_salario = salario * 0.1
else:
    novo_salario = salario * 0.15
apos = salario + novo_salario
print (apos)