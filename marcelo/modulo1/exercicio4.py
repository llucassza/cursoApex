s1 = float(input("Primeiro Salário: "))
s2 = float(input("Segundo Salário: "))
s3 = float(input("Terceiro Salário: "))
s4 = float(input("Quarto Salário: "))

soma1 = (s1 + s2 + s3 + s4)

print(20*"*", "calculadora", 20*"*")
print ("Primeiro Salário: {:.2f} \nSegundo Salário: {:.2f} \nTerceiro Salário: {:.2f} \nQuarto Salário: {:.2f}" .format(s1, s2, s3, s4))
print (f"Soma dos valores: {soma1:.2f}")