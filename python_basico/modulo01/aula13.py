validador = bool

idade = int(input('Digite sua idade:> '))

validador = (idade > 18)
print(f'O usuário é maior de idade:  {validador}')

validador = (idade < 18)
print(f'O usuário é menor de idade:  {validador}')

validador = (idade == 18)
print(f'O usuário tem 18 anos:  {validador}')

validador = (idade != 18)
print(f'O usuário tem uma idade diferente de 18:  {validador}')

validador = (idade >= 18)
print(f'O usuário tem uma idade maior ou igual a 18:  {validador}')

validador = (idade <= 18)
print(f'O usuário tem uma idade maior ou igual a 18:  {validador}')