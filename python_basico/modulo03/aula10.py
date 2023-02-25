var = 1

while var != 0:

    var = int(input("Digite um número que possa calcular o dobro:> "))

    multiplicacao = var * 2

    if var == 0:
        print('O resultado foi nulo')
        

    elif var != 0:
        print(f"o numero digitado foi {var} e o dobro é {multiplicacao}") 