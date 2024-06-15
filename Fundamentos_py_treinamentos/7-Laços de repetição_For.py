# Laço for

lista = [2,6,9,4,0,12,3,7]
for item in lista:
    print(item)


nome = 'Franci'
for letra in nome:
    print(letra)


#Function range
for numero in range(11):      #range(11) posso usar assim também range(1,11) -> valor inicial e final
    print(numero)


#Escrevendo na tela 10 vezes o nome
nome = input('Digite seu nome')
for x in range(10):
    print(f'{x+1} {nome}')


# range(valor_inicial, valor_final, incremento)
for x in range(2,20, 2): #posso utilizar inverso, drecremento, range(20,2, -2):
    print(x)


# laço e if pra verificar se um nome está dentro de um tupla, se estiver não imprimir esse nome
pedras = ('Ruvi', 'Esmerado', 'Quartzo', 'Safira', 'Diamente', 'Turmalina')
for pedra in pedras:
    if pedra != 'Quartzo':
        print(pedra)


pedras = ('Ruvi', 'Esmerado', 'Quartzo', 'Safira', 'Diamente', 'Turmalina')
for pedra in pedras:
    if pedra == 'Quartzo':
        continue #Não vai imprimir a interação atual, mas vai continuar com as proximas 
    print(pedra)