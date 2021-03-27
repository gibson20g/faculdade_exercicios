print('''Escolha o Tipo de Combustivel\nD - Diesel\nE - Etanol\nG - Gasolina''')
combustivel = str(input('Escolha: '))
litros = float(input('Quantos Litros: '))
diesel = 4.486
etanol = 4.719
gasolina = 5.793
if combustivel == 'D' and 20 >= litros:
	tot = diesel * litros
	desc = tot - (tot * 0.02)
	print('O total de conta foi R${:.2f} você recebeu um desconto e pagará somente R${:.2f}'.format(tot, desc))
elif combustivel == 'E' and 20 >= litros:
	tot = etanol * litros
	desc = tot - (tot * 3/100)
	print('O total de conta foi R${:.2f} você recebeu um desconto e pagará somente R${:.2f}'.format(tot, desc))
elif combustivel == 'G' and 20 >= litros:
	tot = gasolina * litros
	desc = tot - (tot * 4/100)
	print('O total de conta foi R${:.2f} você recebeu um desconto e pagará somente R${:.2f}'.format(tot, desc))
elif combustivel == 'D' and litros >= 20:
	tot = diesel * litros
	desc = tot - (tot * 0.04)
	print('O total de conta foi R${:.2f} você recebeu um desconto e pagará somente R${:.2f}'.format(tot, desc))
elif combustivel == 'E' and litros >= 20:
	tot = etanol * litros
	desc = tot - (tot * 5/100)
	print('O total de conta foi R${:.2f} você recebeu um desconto e pagará somente R${:.2f}'.format(tot, desc))
elif combustivel == 'G' and litros >= 20:
	tot = gasolina * litros
	desc = tot - (tot * 6/100)
	print('O total de conta foi R${:.2f} você recebeu um desconto e pagará somente R${:.2f}'.format(tot, desc))
else:
	print('Opção Invalida\nTente Novamente')
