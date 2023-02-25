numero = 0

for cronometro in range(0, 3):

    valor = int(input("digite o numero de inicio:> "))

    numero +=valor 

print(numero)

if numero > 10:
    print (f"A soma dos numeros digitados é {numero}, e a soma é maior do que 10")
else:
    print(f"A soma dos números digitados é {numero}, e a soma não é maior do que 10")
    