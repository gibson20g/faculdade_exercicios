print("escolha uma das opcoes:")
print("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão")
op = int(input("escolha a sua operação:"))
n1 = float(input("qual e o seu primeiro valor:"))
n2 = float(input("qual o seu segundo valor:"))
if op == 1:
    s = n1 + n2
    print("seu valor {} é".format(s,n1,n2))
elif op == 2:
    su = n1 - n2
    print("seu valor {} é".format(su,n1,n2))
elif op == 2:
    su = n1 - n2
    print("seu valor {} é".format(su,n1,n2))
elif op == 3:
    m = n1 * n2
    print("seu valor {} é".format(m,n1,n2))
elif op == 4:
    d = n1 / n2
    print("seu valor {} é".format(d,n1,n2))
else:
    print(" op inválida")
