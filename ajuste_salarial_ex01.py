nome = str(input("Digite o Nome do Funcionario: "))
salario = float(input("Qual é o salário do funcionario?R$: "))
if salario <= 1045:
	print('='*35)
	novo = salario + (salario * 5.26 / 100)
	porcent = 5.26
	aumento = novo - salario
	print("Funcionário {}\nSalário é R${:.2f}, \nPorcentagem de aumento {}% ".format(nome, salario, porcent))
	print("Aumento de R${:.2f}, \nE o novo salário será R${:.2f}".format(aumento, novo))
	print('='*35)
elif 2195 >= salario > 1045:
	print('='*35)
	novo = salario + (salario * 4.32 / 100)
	porcent = 4.32
	aumento = novo - salario
	print("Funcionário {}\nSalário é R${:.2f}, \nPorcentagem de aumento {}% ".format(nome, salario, porcent))
	print("Aumento de R${:.2f}, \nE o novo salário será R${:.2f}".format(aumento, novo))
	print('='*35)
elif 3500 > salario > 2195:
	print('='*35)
	novo = salario + (salario * 2.75 / 100)
	porcent = 2.75
	aumento = novo - salario
	print("Funcionário {}\nSalário é R${:.2f}, \nPorcentagem de aumento {}% ".format(nome, salario, porcent))
	print("Aumento de R${:.2f}, \nE o novo salário será R${:.2f}".format(aumento, novo))
	print('='*35)
elif salario >= 3500:
	print('='*35)
	novo = salario + (salario * 1.79 / 100)
	porcent = 1.79
	aumento = novo - salario
	print("Funcionário {}\nSalário é R${:.2f}, \nPorcentagem de aumento {}% ".format(nome, salario, porcent))
	print("Aumento de R${:.2f}, \nE o novo salário será R${:.2f}".format(aumento, novo))
else:
	print("Algum dado incorreto tente novamente")
