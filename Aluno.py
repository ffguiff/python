class Aluno:
    def __init__(self, nome, matricula):
        #atributos do aluno
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        self.status = "em curso"

    #metodos
    def exibir(self):
        nome = self.nome
        matricula = self.matricula
        notas = self.notas
        status= self.status
        print(nome, matricula, notas, status)

    def cadastrarNotas(self):
        notas = self.notas
        nome = self.nome
        matricula = self.matricula
        for a in range(3):
            notas.append(float(input("inserir notas: ")))
        print("Notas do aluno: ",nome,"de matricula: ",matricula,". Notas:" ,notas)
    
    def calcularMedia(self):
        notas = self.notas
        print(round(sum(notas)/len(notas),2))
        

