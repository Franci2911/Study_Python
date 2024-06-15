#nome -> é o nome que estou atribuindo a minha variavel 
#= -> é o sinal de atribuição ou seja estou atribuindo um valor para minha variavel 
#Franci -> Valor atribuido para variavel 
nome = 'Franci'
print(nome)

media = 0
print(media)

#Declarando variaveis em apenas 01 linha
n1 = n2 = n3 = n4 = 0.0
print(n4)

#Lista de nomes variaveis | Lista de valores variaveis
nome, idade = 'Marcia', 25
print(nome)
print(idade)

estado = True #Variavel do tipo booleano

#Função type para visualizar tipo de dados - comentado geral com ctrl + K + C
# print(type(media))
# print(type(nome))
# print(type(n2))
# print(type(estado))

#Variaveis do tipo complex em python -> Tipos complexos
print(type(1+2j))


# Outra funçao para saber o tipo de um dado 
a = 10
b = 'Sol'
print(isinstance(a, int))
print(isinstance(b,str))
print(isinstance(b,float))

#Verificando se uma variavel é do tipo str ou int ou flot -> Varias verificações juntas
print(isinstance(a, (float,str)))
    # importante lembrar, sempre que eu quiser fazer a verificação de uma variavel com mais de um condição
    # tenho que deixar os types dentro de um ()


# reatribuindo valor para variavel 
a = 40
c = 3
r = a * c #multiplicação
print(r)



