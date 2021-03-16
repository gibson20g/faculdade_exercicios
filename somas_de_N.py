s = 0
c = 0
while True:
	v = int(input('Digite um n para somar ou 0 para mostrar o resultado: '))
	if v == 0:
		break
	c = c + 1
	s = s + v
	mediana = s / c
print('A soma dos numero é: {}'.format(s))
print('A média do aluno é: ', mediana)
