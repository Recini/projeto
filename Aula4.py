from tkinter import *

def click(): 
    texto.configure(text="Ligado")

janela = Tk()

janela.title("Tela Principal")

#janela.iconbitmap("")
janela.geometry("400x300")
janela.resizable(True, True)

texto = Label(janela, text = "Desligado")
texto.pack()

botao = Button(janela, text = "Ligar", command=click)
botao.pack()

janela.mainloop()




