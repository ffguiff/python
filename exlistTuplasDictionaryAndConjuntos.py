lista = []
for a in range(3):
    lista.append(input("nome: "))

'''criar uma função para verificar se o nome descomplica
esta enserido na lista
se foi exibir o nome descomplica
se nao exibir todos os nomes'''

def analise(nome, indice = 0):
    #caso base, indicação para parar
    #percorrer toda a lista (len(lista)) e retornar que nao encontrou
    if indice >= len(lista):
        print ("não esta na lista")
        return False
    #se achar retornara que achou o valor na lista
    if nome == lista[indice]:
        print("esta na lista")
        return True
    #codigo para continuar analisando outros indices da lista
    #reinicia(recursão) a função com novos parametros para analise
    return analise(nome,indice + 1)
    #importante colocar o return para retorn as reposta no final das
    #recursoes(chamdas da função)

analise("gui")
