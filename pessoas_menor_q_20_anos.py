menor_21 = maior_50 = 0
while True:
	idade = int(input("Digite as idades: "))
	if idade < 21:
		menor_21 += 1
	if idade > 50:
		maior_50 += 1
	if idade == -99:
		break
print("Pessoas menor que 20: {} Pessoas ".format(menor_21))
print("Maior que 50: {} Pessoas ".format(maior_50))
