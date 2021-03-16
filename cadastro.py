from tkinter import *
"esse programa serve para abrir janelas"
def funcao_botao():
    n1 = int(caixa_1.get())
    n2 = int(caixa_2.get())
    resultado = n1 + n2
    label_1["text"] = " Você entrou no nosso Aplicativo Entrou e esse é seu resultado: "
    label_1["text"] = label_1["text"] + str(resultado)
janela = Tk()
label_1 = Label(janela, text="Bem Vindo ao *********", font="Arial 20")
label_1.place(x=200, y=200)
label_mais = Label(janela, text="+", font="Arial 30")
label_mais.place(x=420, y=50)
botao_1 = Button(janela, width=25, text="botão", command=funcao_botao, background="green")
botao_1.place(x=200, y=300)
caixa_1 = Entry(janela, background="blue", width=10, font="Arial 30")
caixa_1.place(x=120, y=50)
caixa_2 = Entry(janela, background="blue", width=10, font="Arial 30")
caixa_2.place(x=520, y=50)
janela.geometry("800x600+0+0")
janela.mainloop()
