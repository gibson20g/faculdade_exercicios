idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
cardiaco = int(input("É cardíaco? Aperte 1 (sim) ou 2 (não): "))
gravida = int(input("Está grávida? Aperte 1 (sim) ou 2 (Não): "))
card = "Cardiaco(a)"
buxuda = "GESTANTE"
if idade < 16 and peso < 50:   #while antes de cardiaco gravida, break  try/ except
	print("peso e idade não autorizadas MINIMO!!!!!")
elif idade > 69 and peso > 100:
	print("peso e idade não autorizadas MAXIMO!!!!!")
elif (idade < 16) and (peso > 100):
	print("IDADE minima e peso maximo")
elif (idade > 69) and (peso < 50):
	print("idade maxima e peso minimo")
elif (69 > idade > 16) and (100 > peso > 50) and (cardiaco == 2) and (gravida == 2):
	print("Você cumpre todos requisitos, ESTÁ AUTORIZADO")
elif (69 > idade > 16) and (100 > peso > 50) and (cardiaco == 1) and (gravida == 1):
	print("Você não cumpre todos requisitos, você é {} e {}".format(card, buxuda))
elif (69 > idade > 16) and (100 > peso > 50) and (cardiaco == 1) and (gravida == 2):
	print("Você não cumpre todos requisitos, você é {}  ".format(card))
elif (69 > idade > 16) and (100 > peso > 50) and (cardiaco == 2) and (gravida == 1):
	print("Você não cumpre todos requisitos, você é {}  ".format(buxuda))
else:
	print("VOCÊ NÂO ESTA DENTRO DE ALGUMA EXIGENCIA, POR ISSO está NEGADO O ACESSO")



"""
elif (idade < 16) and (peso < 50) or ( idade > 16) and (cardiaco == 2) and (gravida == 2):
	print("SUA idade {} anos e seu peso {}kg são insuficientes".fomart(idade, peso))
elif (69 < idade) and (100 < peso) and (cardiaco == 2) and (gravida == 2):
	print("Sua IDADE {} anos e seu PESO {}KG estão acima do limite".format(idade, peso))
"""