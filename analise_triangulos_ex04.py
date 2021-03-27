r1 = float(input('Primeiro Segmento'))
r2 = float(input('Segundo Segmento'))
r3 = float(input('Terceiro Segmento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('Os segementos acima Podem formar Triângulos')
	if r1 == r2 == r3:
		print('E É UM TRIÂNGULO ^^EQUILATERO^^')
	elif r1 != r2 != r3 != r1:
		print('ESSE JÁ É UM ^^ESCALENO^^')
	else:
		print('^^ISÓSCELES^^ certeza')
else:
	print('Os segementos Não Formam Triângulo')
