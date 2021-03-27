from time import sleep
nm = int(input(" Digite um número qualquer "))
result = (nm % 2)
print('Analisando resposta...')
sleep(3)
if result == 0:
    print('O número {} é par'.format(nm))
else:
    print('O número {} é ímpar'.format(nm))
