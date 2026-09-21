ano_atual = int(input('Qual é o ano atual?: '))
ano_nascimento = int(input('Qual é seu ano de nascimento?: '))
idade = ano_atual - ano_nascimento
if idade >=18:
    print ('A sua idade é: ', idade)
    print ('Você pode tirar a sua CNH!')
else:
    print ('A sua idade é: ', idade)
    print ("Você não pode tirar a sua CNH.")