from time import sleep
numero = int(input("Digite um número:> "))

poli = "*" *20

print(f"{poli}cabeçalho for {poli}")

#zero representa o inicio. variavel numero representa fim 

for tamanho_for in range (0, numero+1):
    print(tamanho_for)