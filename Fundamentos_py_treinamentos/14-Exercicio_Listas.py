#Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses
#valores em uma lista. Na sequência, exiba na tela os elementos da lista em ordem alfabética, um por
#linha,usando um laço de repetição for.

# [] Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele

bebidas = list()
for i in range(1,6,1):
    nome_bebidas = input('Digite o nome das suas 5 bebidas favoritas: ')
    bebidas.append(nome_bebidas)
print(sorted(bebidas))
print(sorted(bebidas, reverse=True))

print(f'\nBebidas escolhidas: ')

for i in bebidas:
    print(i)
print(f'\nSaúde')