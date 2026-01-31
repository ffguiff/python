'''fazer sistema de verificação de maioridade usando
fuçoes'''

anoAtual = 2026
anoDeNascimento = int(input("digite seu ano de nascimento: "))
MAIORIDADE= 18 

def maioridade():
    idade = anoAtual - anoDeNascimento
    if idade >= 18:
        return "você é de maior."
    else:
        return "você é de menor."

print(maioridade())

'''contagem de 0 a 10 com recursão
contagem de 10 a 0 '''

def contagemCrescente (n):
    #parametro para parar se for igual a 10 para o codigo e retorna 10
    '''enquanto n for menor que 0 '''
    if n < 0:
        return
    
    '''executar isso'''
    contagemCrescente(n - 1)
    print(n)

contagemCrescente(10)

def contagem(n):
    if n > 10:
        return
    contagem(n + 1)
    print (n)

contagem(0)