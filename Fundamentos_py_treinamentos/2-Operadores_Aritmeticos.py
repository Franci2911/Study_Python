#Aula realizada no terminal 

# + soma
# - subtração
# * Multiplicação
# / Divisão
# // Divisão inteira
# % Módulo(mod) retorna o resto de uma divisão inteira 11%2=1
# ** potenciação -> a=10 (a ** 2)=100
                   #a=10 (a ** 5)=100000


#Ordem de precedências
# Parênteses
# Potenciação
# Multiplicação / Divisão
# Soma / Subtração
# Esquerda para Direita

x = y = z = 0
x = 7
y = 9

z = x + y
print(z)

#Construindo uma msg para imprimir, ou seja uma mensagem de saída
print('A soma dos dois valores é: ' ,z)

#Função input() -> a função input sempre vai retornar uma string; 
#Utilizando o Casting -> convertendo string para inteiro
x = int(input('Digite um numero: '))
y = int(input('Digite um numero: '))
k = x+y

print('A soma dos valores é: ', k)