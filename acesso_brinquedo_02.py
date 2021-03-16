idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
cardiaco = int(input("É cardíaco? Aperte 1 (sim) ou 2 (não): "))
gravida = int(input("Está grávida? Aperte 1 (sim) ou 2 (Não): "))
card = "Cardiaco(a)"
gravi = "GESTANTE"

if (idade < 16) and (peso < 50):
    print("Peso e idade não autorizadas(menores que o esperado)",idade,"< 16","e",peso,"< 50")
elif (idade > 69) and (peso > 100):
    print("Peso e idade não autorizadas(Maiores que o esperado)",idade,"> 69","e",peso,"> 100kg")
elif (idade < 16) and (peso > 100):
    print("Idade inferior e peso maior que o limite",idade,"< 16","e",peso,"> 100kg")
elif (idade > 69) and (peso < 50):
    print("Idade superior ao limite e peso menor que 50",idade,"> 69","e",peso,"< 50kg")
elif  (cardiaco == 1) and (gravida == 1):
    print("Você não está autorizado(a) a brincar, pois é tanto cardíaco como grávida")
elif (cardiaco == 1) and (gravida == 2):
    print("Você não está autorizado(a) a brincar, pois é cardíaco")
elif (cardiaco == 2) and (gravida == 1):
    print("Você não está autorizado(a) a brincar, pois está grávida")
elif (cardiaco == 2) and (gravida == 2):
    print("Você está autorizado(a) a brincar")
else:
    print("Não é autorizado pois nçao cumpre algum requisito")
