# Encadeamento de laços de repetições 

# for cont_ex in range(1,6):
#     print(f'\nRodada: {cont_ex}')
#     for cont_int in range(5,0,-1):
#         print(f'Valor: {cont_int}')
# print('Fim do laços de repetições')


import random

for a in range(1,5):
    print(f'\nconjunto: {a}')
    for b in range(5):
        num = random.randint(1,100)
        print(f'valor: {num}')

# random -> è um modulo 