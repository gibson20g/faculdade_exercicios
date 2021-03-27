from time import sleep
print("=" * 30)
print('Concessionaria Gibson`s')
print("=" * 30)
sleep(2)
divida = int(input("Olá, Informe o valor da sua Divida R$: "))
parcelas = int(input("Agora informe a quantidade de parcelas restantes N°"))
juros = divida / parcelas
sleep(2)
print("Aguarde enqunto cálculamos sua divída ")
sleep(3)
if 4 >= parcelas >= 1:
  print("O valor de cada parcela reajustada com juros é de", ((juros / 100) * 4 + (juros)))
  print("O novo valor total da dívida é de;", ((divida / 100) * 4 + (divida)))
elif 4 < parcelas < 7:
  print("O valor de cada parcela reajustada com juros é de", ((juros / 100) * 6.8 + (juros)))
  print("O novo valor total da divida é de:", ((divida / 100) * 6.8 +(divida)))
elif 7 < parcelas <= 10:
  print("O valor de cada parcela reajustada com juros é de:", ((juros / 100) * 7.2 + (juros)))
  print("O novo valor total da divida é de:", ((divida / 100) * 7.2 + (divida)))
