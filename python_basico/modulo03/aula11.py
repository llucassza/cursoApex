from time import sleep

media = 0

while media < 7:

    nome = input("Digite seu nome:> ")
    sobrenome = input("Digite seu sobrenome:> ")
    idade = int(input('Digite sua idade:> '))

    for lista in range (0,2):
        nota = int(input('Digite a sua nota:> '))

        lista_notas = [nota]

        media = sum(lista_notas)/ len(lista_notas)


    if media >= 7:
        sleep(2)
        for c in range (0, 10):
            print('*')
            sleep(1)
        situacao = 'parabéns, voce foi aprovado'

    elif media < 7:
        situacao = 'Reprovado tente novamente'

dicionario = {'nome': nome, 'sobrenome': sobrenome, 'idade': idade, 'media': media, 'situacao': situacao}

print (f"{dicionario['nome']} {dicionario['sobrenome']} {dicionario['idade']} {dicionario['situacao']}")