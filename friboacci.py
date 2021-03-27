x = int(input('Você quer a Soma de Quantos termos ? '))
x1 = 0
x2 = 1
c = 3
while c <= x:
	x3 = x1 + x2
	x1 = x2
	x2 = x3
	c += 1
	print(x)
