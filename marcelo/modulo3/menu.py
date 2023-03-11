from controller import salvar, listar


def menu():
    print("*"*25, "MENU CALCULADORA", "*"*25)
    cond = "sim"
    while cond == "sim":
        text = input("1 - Digite o número 1 para cadastrar o usuário \n2 - Digite o número 2 para listar os usuários: ")
        if text == ("1"):
            nome = str(input("Digite o nome do usuário: "))
            salvar(nome)
        else:
            print("lista nomes \n", listar())
        cond = input("deseja continuar? \n Sim \n Não \n : ")






            # texte = input("1 - Digite o número um para cadastrar o usuário \n2 - Digite o número 2 para listar os usuários: ")
            # if texte == 1:
            #     nome = str(input("Digite o primeiro nome: "))
            #     salvar(nome)
            # elif texte == 2:
            #     print ("acabou")
            # cond = input("Deseja continuar \n Sim \n Não \n : ")

menu()
print ("voce saiu da aplicação")
