'''a= input("digite um numero: ")
print(a + 5)'''
#deveria ser 15 se inserirmos 10, mas da erro

#o print leva em consideração o numero como um testo
#se somar com  um numero ele não ira realizar corretamente 

#para corrigir o erro deve ser adicionado a int()

a = int(input("digite um numero: "))
print(a + 5)

b = float(input("digite numero com decimal:"))
print(b + 0.5)