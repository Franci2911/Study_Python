#Tuplas -> Também é uma estrutura de dados muito utilizado em python 

# Diferenças importante da lista, as tuplas são imutaveis, e dependendo da operação ela é mais rapida

#Criando uma tupla
tupla = (2,5,4,6)
print(tupla)

halogenios = ('F', 'CL', 'Br', 'I', 'At')
print(halogenios)


#Quantidade de elementos dentro dessa tupla
print(len(halogenios))


#Concatenando 2 tuplas diferente
tupla_2 = ('He', 'Ne', 'Ar', 'Xe', 'Rn')

elementos = halogenios + tupla_2
print(elementos)

#Descobrindo quantas vezes um valor aparece dentro de um tupla 
t1 = (1, 4,5,6,7,8,9,9,9,9,0,1,2,3,4,6,7,48,9,245,345,5)
print(t1.count(9))

#Pegando apenas alguns elementos da mina tupla 
print(t1[0:2]) #os 2 primeiros elementos
print(t1[:3])  #a partir do primeiro elemento até o elemento 3
print(t1[-2:])  #a partir do penultimo elemento

#Verificando se tenho um valor dentro de uma tupla 
print('Ne' in tupla_2)


#Operadores aritmeticos dentro de uma tupla
print(sum(t1))    #somando os valores de uma tupla
print(max(t1))    #somando os valores de uma tupla
print(min(t1))    #somando os valores de uma tupla


#Operadores não disponíveis em tuplas:
# .sorted()
# .append()
# .reverse()
# .pop() 
#Ou seja todos os metodos de alteração de um lista não podem ser usados em tuplas 



#posso fazer iteração com os laçoes de repetições 
for i in elementos:
    print(f'Elemento quimico: {i}')


#Criando uma lista a patir de um tuplas 
grupos17 = list(elementos)
print(grupos17)


#Também consigo criar um tupla a partir de uma lista 
grupo18 = tuple(grupos17)
print(grupo18)


#Classificando a tupla utilizando uma função 
print(sorted(grupo18))
print(sorted(grupo18, reverse=True))












