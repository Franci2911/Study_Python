import mod_func as mf


# -> instruçao importante, é uma instrução condicional usado para controlar o fluxo do codigo 

# __name__  -> é uma variavel que tem o nome do modulo atual

# '__main__' -> Quando o modulo é executado como se fosse o programa principal o valor de __name__ 
# é definido como __main__ ; quando ele é importante o valor do __name__ é definido __main__


if __name__ == '__main__':
    mf.mensagem_feliz()

msg = mf.mensagem_feliz()
print(msg)

msg_2 = mf.mensagem_triste()
print(msg_2)