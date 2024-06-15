x = y = z = False
n1 = n2 = 0

print('Digite um numero: ')
n1 = int(input())
n2 = int(input('Digite o segundo numero: '))

x = n1 == n2
print('São iguais? ', x, '\n') #Caracter de escape '\n' ->quebra de linha

z = n1 > n2
print(n1, ' é maior que ', n2, '? ', z, '\n')


y = n1 != n2
print('São diferentes ? ' + str(y)) #+ é um sinal de concatenação em string
