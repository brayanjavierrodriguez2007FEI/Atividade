litro = float(input("Quantos litros foram abastecidos?: "))
valor = float(input("Qual é o valor de cada litro?: "))
valor_pago = litro * valor
if valor_pago > 200:
    print ('Atenção: Compra com desconto especial disponível no caixa!')
    valor_pago = valor_pago - valor_pago * 0.10
    print ('O valor total após o desconto será de: ' ,valor_pago)
else:
    print ('O valor total será de: ', valor_pago)