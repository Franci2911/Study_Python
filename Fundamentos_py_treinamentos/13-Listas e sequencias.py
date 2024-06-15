#Sequencias em python 

#Listas -> é a mais comum, uma lista representa uma sequencia de valores armazenada na memoria

# sintaxe correta: nome_lista = [valores]

notas = [5,7,2,6,9]
print(notas)


#Cada item da lista pode ser acessado individualmente, começando pelo índice ZERO
n1 = [1,2,3,4]
n2 = [5,6,7,8,9,10]
valores = n1 + n2
print(valores)
print(type(valores))

#Acessando só o primeiro item da lista 
print(valores[0])
print(valores[-1]) #Vai trazer o ultimo valor de uma lista -2 vai trazer 9 e assim por diante.

#Alterando valores de uma lista 
valores[0] = 100
print(valores)

#Acessando valores sequencias de uma lista 
print(valores[0:2]) # A partir do primeiro valor traga 2 valores 

#Acessando valores sequencias de uma lista -> A parte do indice no meio da lista
print(valores[2:5]) # A partir do primeiro valor traga 2 valores 

#Acessando do penultimo até o final da minha lista
print(valores[-2:]) # A partir do primeiro valor traga 2 valores 


#Function para manipular uma lista 
#Descobrindo a quantidade de elementos de uma lista 
print(len(valores))                #retorna o tamanho dos elementos da lista
print(sorted(valores))             #Vai ordernar a lista em ordem crescente
print(sorted(valores, reverse=True))             #Vai ordernar a lista em ordem decrescente
print(sum(valores))                              #Somando os valores dentro da minha lista
print(min(valores))                              #Encontrando o menor valor
print(max(valores))                              #Encontrando o maior valor


#Metodos para manipular o valor de uma lista, realmente mexendo dentro da lista 
valores.append(550) #Acrescetando um valor após o ultimo índice da lista dentro da lista 
print(valores)

valores.pop() #Remove o ultimo valor da lista
print(valores)

valores.pop(3) #Vai remover um elemento da lista a partir do índice 
print(valores)

valores.insert(1,21) #Inserindo o valor 21 na posiçao e da lista
print(valores)

print(12 in valores) # vai retornar True ou False

#A Gente consegui fazer iteração dentro de uma lista utilizando FOR
# maneiras de criar lista vazia
planetas_1 = []
planetas_2 = list()

planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Neturno']
for i in planetas:
    print(i)






