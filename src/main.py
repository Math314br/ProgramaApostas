#aqui é o programa pricincipal aonde tudo ira rodar.
from tkinter import *

janela = Tk()

class Applicação():
    def __init__(self):
     self.janela= janela
     self.tela()
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

Applicação()