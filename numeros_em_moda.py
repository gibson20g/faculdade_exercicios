x = int(input("Digite o valor um: "))
y = int(input("Digite o valor dois: "))
z = int(input("Digite o valor três: "))
if z > y > x:
	print("crescente")
elif x > y > z:
	print("não está em ordem crescente")
else:
	print("Fora de ordem, nem crescente nem decrescente")
