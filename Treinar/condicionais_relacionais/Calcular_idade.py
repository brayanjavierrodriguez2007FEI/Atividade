ano_atual = int(input('Qual é o ano atual?: '))
ano_nascimento = int(input('Qual é seu ano de nascimento?: '))
idade = ano_atual - ano_nascimento
if idade >=18:
    print("Você pode tirar a sua CNH!")
else:
    print ("Você não pode tirar a sua CNH.")