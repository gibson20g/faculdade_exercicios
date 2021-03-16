print('*'*15)
print('Cálculadora')
print('*'*15)
print('='*20)
print('''Escolha Uma opção\n1 - Soma\n2 - Multiplicação\n3 - Divisão\n4 - Subtração''')
print('='*20)
op = float(input('Digite Sua Opção: '))
if op == 1:
	soma_n_1 = float(input('Digite o um valor: '))
	soma_n_2 = float(input('Digite o outro valor: '))
	somaTot = soma_n_1 + soma_n_2
	print('O valor da Soma é {:.2f}'.format(somaTot))
	print('Programa Encerrado ')
elif op == 2:
	multi_n_1 = float(input('insira o Valor para Multiplicar: '))
	multi_n_2 = float(input('Insira Outro Valor Para Multiplicar: '))
	multi_fim = multi_n_1 * multi_n_2
	print('O Valor da multiplicação é {:.2f}'.format(multi_fim))
	print('Programa Encerrado ')
elif op == 3:
	divi_n_1 = float(input('valor 1 p/Dividir '))
	divi_n_2 = float(input('Valor 2 p/Dividir '))
	diviResul = divi_n_1 / divi_n_2
	print('O valor da divisão é: {:.2f}'.format(diviResul))
	print('Programa Encerrado ')
elif op == 4:
	sub_n_1 = float(input('numero  para subtrair!: '))
	sub_n_2 = float(input('outro numero subtrair: '))
	sub_reali = sub_n_1 - sub_n_2
	print('A subtração é:{:.2f} '.format(sub_reali))
	print('Programa Encerrado ')
else:
	print('Opção Inválida!!!!Tente Novamente')
	print('Programa Encerrado ')
