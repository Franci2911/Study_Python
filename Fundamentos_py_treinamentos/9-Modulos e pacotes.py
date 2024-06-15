# Modulos e pacones em python 

# -> Adicionando funcionalidades a uma aplicação para facilitar a codificação 

# -> Instalando pacotes utilizando pip

#   [] python3 -m pip list      ->Vai trazer a lista de pacotes que estou utilizando
#   [] pip install matplotlib    ->instalando um pacote 
#   [] pip uninstall matplotlib    -> Desintalando um pacote 

#Importe genericos
import math   #Modulo de function matematicas 
print(math.sqrt(81))

#Import de especificas -> Importante apenas 01 function de um pacote 
from math import sqrt, sin
print(sqrt(81))

#Importe universal ->não muito recomendado
from math import *
print(sqrt(81))

#Alias
import math as m 
print(m.sqrt(81))