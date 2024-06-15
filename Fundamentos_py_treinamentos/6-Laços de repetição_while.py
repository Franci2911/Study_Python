# While -> Enquanto
# Enquanto for verdade ele executa o loop, só para quanto o teste logico retorna FALSE 

# Imprimir numero até 10
num = 1
while (num <= 10):
    print(f'Numero: {num}')
    num += 1    #encremento 


# Se eu não souber onde devo para o laço eu utilizo o laço: FOR
# nome sig um espaço na memoria vazio
nome = 'nome'

while True:
    print('Digite seu nome, ou x para parar: ')
    nome = input()

    print(f'Bem-vindo, {nome}')

    if nome == 'x' or nome == 'X':
        break   #Break -> vai para o bloco e finalizar o laço while
print('Até logo')