import random as rd
# random significa aleatorio em ingles

valor = rd.randint(1,10)
print(f'Numero aleatorio é: {valor}\n')


#Gerando varios numeros aleatorios com random + função for 
print('Gerar cinco numeros aleatorios entre 1 e 50 ')
for i in range(1,6,1):
    num = rd.randint(1,50)
    print(f'O {i}ª numero é: {num}')
print('Todos os numeros, foram gerados com sucesso!')


#Gerando numeros de pontos float com random 
print('Gerar 1 numero aleatorio entre 0 e 10 do typo float')
valor_aleatorio = rd.random()     #Arredondando os valores com varias casa decimais
print(round(valor_aleatorio,2))

#Gerando numeros floats aleatorio determinando inicio e fim com a função rd.uniform()
v = rd.uniform(1,200)
print(round(v, 4))

#Lista de valores pré-criada e utilizando uma function random para escolher um numero da lista 
lista = [4,55,63,66,134,66,3234,5323,2432,1,2,3,6,7,3,8,9]
escolhido = rd.choice(lista)
print(f'O numero escolhido pelo sistema foi: {escolhido}')

#Escolhendo varios valores da lista 
varios_escolhido  = rd.sample(lista, 5)
print(f'Numeros escolhidos: {varios_escolhido}')

#Embaralhando os numeros de uma lista com um function random 
print(f'Exibir a lista original : {lista}')
print(f'Embaralhar a lista e exibi-la :')
e = rd.shuffle(lista)
print(lista)
