#Algoritmo para validar 2 informações 

#Exemplo para operador logico -> AND
idade, altura = 15, 1.75
resultado = (idade >= 18) and (altura >= 1.70)

msg = 'Pode participar do evento? ' + str(resultado)
print(msg)



#Exemplo para operador logico -> OR
#Programa de disparo de alarme 
porta = 'a'
janela = 'a'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarma disparado: ' + str(alarme)
print(msg)


#Exemplo para operador logico -> NOT
# O operador NOT inverte o estado logico
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)
