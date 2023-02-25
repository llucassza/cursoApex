from time import sleep

nome = input("Digite seu nome:> ")
sobrenome = input("Digite seu sobrenome:> ")
idade = int(input("Digite sua idade:> "))

for lista in range (0,2):
    nota = int(input("Digite a sua nota:> "))

    lista_notas = [nota]
    media = sum(lista_notas)/len(lista_notas)