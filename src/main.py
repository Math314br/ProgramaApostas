#aqui é o programa pricincipal aonde tudo ira rodar.
from tkinter import *

janela = Tk()

class Applicação():
    def __init__(self):
     self.janela= janela
     self.tela()
     self.frameTELA()
     janela.mainloop()
    def tela(self):
       #TITULO PRINCIPAL DO PROGRAMA
       self.janela.title("Simulador De Bancas")
       #plano de fundo do programa pode ser uma foto ou uma cor.
       self.janela.configure(background= "#C0C0C0")
       #dimensão que janela inicia
       self.janela.geometry("730x1180")
       #se tela é responsiva ou nao se tiver true é, se tiver false nao é
       self.janela.resizable(True,True)
       #Escolha tamanho maximo da tela
       self.janela.maxsize(width=730, height=1180)
       #Escolha tamanho minimo da tela
       self.janela.minsize(width=600, height= 900)
    #esse frame sera basicamente as bordas do programa apenas uma janela basica
    def frameTELA(self):
       self.frame1 = Frame (self.janela, bd= 3, bg="#C0C0C0", highlightthickness=6, highlightbackground="black")
       self.frame1.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
       
       

Applicação()