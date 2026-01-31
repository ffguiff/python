#progamação orientada a objetos
class Pessoa:
    #atributos são variaveis
    nome = "gui" 
    idade = 0
    #metodo = função
    def exibir(self , nome , idade):
        print(nome ,idade)
    #self = use o valor da propria class

    #item de seguraça
    '''pega o dado nao mais direto da class mais primeiro pelo
    metodo'''
    #GET
    @property
    def nome (self):
        return self.nome
    #SET
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    #metodo construtor 
    ''' você definira novos valores que seram iniciados ao chamar a class
    por mais q ela tenha um valor ja inserido nala ele 
    será anulado e o novo valor definido será o principal'''
#mais para prover camada de bloquei de falhas

    #ex:
    # def __init__(self, nome , idade):
    #     self.nome = nome
    #     self.idade = idade