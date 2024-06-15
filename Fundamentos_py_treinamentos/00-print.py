#sintaxe:
# print(objetos, argumentos)

mensagem = 'Function print'
print(mensagem)

print('aula de python')

#Argumentos
sexo = 'masc'
print('Franci Miller - ', sexo)

#Concatenar strings
# nome = input('Digite seu nome: ')
# print('ola '+ nome + ' Bem-Vindo ao curso de python')


# Por padrão o print faz uma quebra de linha nos casos com mais de um print, removendo a quebra
# end='' -> remove a quebra de linha
print('Imprimir a msg e muda de linha')
print('Permanece na mesma linha ', end='')
print('continuo na mesmo linha')

# String .format
nome = 'Miller'
idade = 35

msg_formatada = 'O nome dele é {0} e ela tem {1} anos'.format(nome, idade)
print(msg_formatada)


#melhor forma de usar o print utilizando: fString
nome = 'Fabio'
peso = 100
print(f'O nome dele é {nome} e ele pesa {peso} quilos')

#Dentro da fString podemos executar expressões dentro dela 
a = 10
b = 15
print(f'A soma de {a} + {b} é igual: {a+b}')

#Formatar numeros float com fString
valor = 125.123456
print(f'O valor é {valor:.3f}')   #.2f -> .2 sig 2 casas decimais, f sig que é do tipo float

#fString também podemos utilizar caracteres de escape
valor = 125.123456
print(f'O valor é \'{valor:.3f}\'')    #\' -> Vai imprimir o caracter '

#fString também permiti a tabulação 
nome = 'João'
idade = 43
print(f'O nome:{nome} \t idade:{idade}')  #\t -> Vai criar uma tabulação, normalmente conhecido com caracter de escape




