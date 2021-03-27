print('Olá, Vamos Calcular seu Indice de Massa Corporaal')
peso = float(input('Qual seu Peso em kg ? '))
altura = float(input('Qual Sua Altura ?  '))
imc = peso / (altura ** 2)
print('O Seu IMC é de {}'.format(imc))
if imc < 18.5:
	print('Abaixo do Peso')
elif 18.5 <= imc < 24.99:
	print('Peso dentro do NORMAL')
elif 24.99 <= imc < 34.99:
	print('ACIMA do PESO')
elif imc >= 40:
	print('ESTÁ com OBSIDADE, PROCURE UM MÉDICO')
else:
	print('Dados não correpondentes para cálculo')
print('A tabela que usamos de referência foi \n')
print('''Entre 18.5 e 24.99: peso normal
Entre 25 e 29.99: Acima do peso
Entre 30 e 34.99: Obesidade ''')
