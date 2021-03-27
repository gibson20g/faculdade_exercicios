numero = int(input('Digite um valor inteiro entre 10 e 100 '))
if numero % 4 == 0 and numero % 5 == 0:
	print('O numero {} é divisivel por 4 e 5 '.format(numero))
elif numero % 5 == 0:
	print('Numero divisivel só por 5, numero digitado foi {}'.format(numero))
elif numero % 4 == 0:
	print('O número digitado é divisilvel por 4 "{}" "!'.format(numero))
elif numero % 4 != 0 and numero % 5 != 0:
	print("NÃO DIVISIVEL POR 4 nem por 5")
