from atividade01 import soma, sub, mult, div

def menu():
    print("*"*25, "CALCULADORA", "*"*25)

    cond = "sim"
    while cond == "sim":
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        everton = soma(n1,n2)
        luciano = sub(n1,n2)
        jose = div(n1,n2)
        marcelo = mult(n1,n2)

        print ("Soma: {} \nSubtração: {} \nDivisão: {} \nMultiplicação: {}".format(everton, luciano, jose, marcelo))

        cond = input("deseja continuar \n SIM \n NÃO \n : ")

menu()