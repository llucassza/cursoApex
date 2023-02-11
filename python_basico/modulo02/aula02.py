n1 = float(input('digite a nota:> '))
n2 = float(input('Digite a nota:> '))

media = (n1+n2) /2

# if media >= 7:
#     print('Parabéns você está aprovado')
# else:
#     print('infelizmente você reprovou')

print('parabens voce atingiu a media: ' if media >=7 else 'infelizmente você reprovou')
print('sua media foi {:.1f}'.format(media))