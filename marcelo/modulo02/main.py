from calculadora02 import calculadora

def menu():
    cond = "sim"
    while cond == "sim":
        n1 = int(input("Digite o salário: "))
        n2 = int(input("Digite o salário: "))
        n3 = int(input("Digite o salário: "))
        n4 = int(input("Digite o salário: "))
        cond = str(input("Deseja continuar?: \n Sim \n Não "))
        resultado = calculadora(n1, n2, n3, n4)
        print(f"A soma dos ultimos 4 salários é: {resultado}")

menu()

    