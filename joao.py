# Calcule o peso e a altura de uma pessoa, calcule o IMC
# Entre 18.5 e 24.99
# Entre 25 e 29.99
# Entre 30 e 34.99

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = (peso/(altura**2))
if 18.5 <= imc <= 24.99:
  print('O Seu IMC {:.2f} é de uma pessoa normal'.format(imc))
elif 25 <= imc <= 29.99:
  print('Seu IMC {:.2f} é de uma pessoa acima do peso'.format(imc))
elif 30 <= imc <= 34.99:
  print('Seu IMC {:.2f} é de uma pessoa obesa '.format(imc))
else:
  print('não foi possivel calcular')

