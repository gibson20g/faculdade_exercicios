print('Olá, vamos ser se Você tem a Idade Necessária')
ano_nascimento = int(input('informe o Ano de nascimento: '))
ano_atual = int(input('Informe o ano atual: '))
idade = ano_atual-ano_nascimento
if idade < 18:
	print('Você é menor de idade')
elif idade > 18:
	print('vcoê é maior de idade')
else:
	print('aconteceu algo de errado, tente novamente')
