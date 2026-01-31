# if/else
# March
# ternarios 
'''se chover sair com guarda chuvas, 
se nao chover nao nao sair com guarda chuvas'''

chuva = True

if chuva == False:
    print ("não sair com guarda chuvas")
else:
    print("sair com guarda chuvas.")


'''definindo se é maior de idade ou nao'''

# idade = int(input("digite sua idade: "))

# if idade > 18:
#     print("maior de idade")
# elif idade == 18:
#     print("fico de maior rescentemente")
# else:
#     print("de menor")

# ternario

'''um otimização do if \ else. otimo para quando se tem apenas 2 
condicionais'''
'''voce condença em uma unica linha de codigo'''

idade = int(input("digite sua idade: "))
print ("é maior de idade") if idade>=18 else print("menor de idade")

#Macht (switch case)

''''''
a= "guilherme"
match a:
    case "antonio":
        print("não é o guilherme é sim o antonio")
    case "guilherme":
        print("é o guilherme")
    case "pedro":
        print("é o pedro e não o guilherme")
