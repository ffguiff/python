# exercicio

'''deve pedir ao usuario para digitar ano de nascimento
ano atual
decubra se o usuario é maio de idade
se for maior de idade pede titulo de eleitor
se nao pede um documento do responsavel'''

ano_de_nascimento = int(input("digite seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_de_nascimento

print("titulo de eleitor.") if idade >= 18 else print("documento do responsavel")