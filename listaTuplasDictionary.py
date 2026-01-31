#lista
a = [1,2,3]

#tuplas é o mesmo que a lista so que com valores imutaveis
tupla = (1,2,3,4,5,6,7,8,9,0)
if 87 in tupla:
    print ("existe")
else:
    print("não existe")

#dicionario
'''indice procurado pelo nome é nao melo numero'''
#muito ultilisado para analise de dados 
lista = {"nome": "guilherme", "sobrenome": "ferreira"}
print(lista["nome"], lista["sobrenome"])

#conjuntos
b={1,3,5}
c={2,4,6}

print(set(b.intersection(c)))
print(set(b.difference(c)))

