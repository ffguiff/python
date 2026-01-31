'''diretor de escola precisa de cadastrar aluno com dados:
nome, cpf, matricula
para cada aluno cadastrado pode lançar 3 notas
se a media atinginda for maior ou igual a 6, printar aluno fulano 
"aprovado seu diploma tera os seguinte dados: lista de dados do aluno"
 ou caso for menor que 6 lançar nova nota adicional e adicionar a media 
 se a nova media for inferior a 6 aluno reprovado'''

nome = []
cpf = []
matricula = []
nota = []

nome.append(input("digite o nome do aluno: "))
cpf.append(int(input("digite o cpf do aluno: ")))
matricula.append(int(input("digite a matricula do aluno: ")))

for a in range(3):
     nota.append(float(input("nota do aluno: ")))

#round(calculo, numero de casas decimais)
media = round((nota[0]+ nota[1]+ nota[2])/3,3)
print(media)

if media < 6:
     nota.append(float(input("nota complementar: ")))
     print(nota)
     novaMedia = round((nota[0]+ nota[1]+ nota[2]+ nota[3])/4,3)
     print(novaMedia)

if media >= 6.0 or novaMedia >= 6.0:
     print("aluno aprovado. Parabéns")
     print("Estes seram os dados impressos no seu certificado:")
     print("o aluno ",nome, "de cpf: ",cpf, "matricula: ", matricula, "concluio o ensino médio.")
else:
     print("aluno reprovado.")

#para uma pessoa o codigo funciona agora devo adptalo
#para mais alunos