def teste():
    txt = "imprimir resultado"
    return txt
print(teste())

#soma com parametros
def soma(a , b):
    c = a + b
    if c % 2 == 0:
        return "par"
    else:
        return "impar"

print(soma(4,9))

#função recursiva
'''fatorial
5! = 5 * 4 * 3 * 2 * 1 = 120'''

def fatorial (n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))