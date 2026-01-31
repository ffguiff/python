import requests
r = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")

'''caso queira trabalhar com os dados da internet'''

#caso queira manipular os dados da web 
#preciso criar um novo arquivo que ira receber os dados trazidos
with open("teste2.txt", "wb") as teste:
    teste.write(r.content)
    #wb = write binary (ler em binario)