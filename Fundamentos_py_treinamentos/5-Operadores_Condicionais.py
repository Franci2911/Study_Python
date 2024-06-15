#Desvios condicionais, expressão IF

n1 = n2 = 0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#Calculando a média aritmética das notas
media = (n1 + n2) / 2

# No If o caracter ':' vai determinar tudo que está dentro daquele bloco, a identação vai dizer o que está no bloco
# Condional SIMPLES
if (media >= 7):
    print('Resultado: Aprovado')
    print('Parabéns!')
print('Sua média é {}' .format(media))


#Condional COMPOSTO
if (media >= 7):
    print('Resultado: Aprovado')
    print('Parabéns!')
else:
    print('Aluno Reprovado...')
print('Sua média é {}' .format(media))


#Condicional ENCADEADA
if (media >= 7):
    print('Resultado: Aprovado')
    print('Parabéns!')
elif (media >= 5):
    print('Você está de recuperação!...')
else:
    print('Aluno Reprovado...')
print('Sua média é {}' .format(media))