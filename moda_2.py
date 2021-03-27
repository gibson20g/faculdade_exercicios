import statistics
amostra = []
while True:
	n = int(input('Digite Valores de 0 a 10 varias vezes: '))
	amostra += [n]
	if n == 0:
		break
moda = statistics.mode(amostra)
print('Moda', moda)
