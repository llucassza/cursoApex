numero = int(input("Digite o numero que você deseja saber a tabuada:> "))

for tabuada in range (1,11):
    print('{} x {} = {}'. format(numero, tabuada, numero*tabuada))