#aqui é o programa pricincipal aonde tudo ira rodar.
from tkinter import *

janela = Tk()

class Applicação():
    def __init__(self):
     self.janela= janela
     self.banca = 100 # valor da banca inicial
     self.tela()
     self.frameTELA()
     self._banca()
     self.botao_banca()
     self.ativar_edicao()
     self.atualizar_banca()
     janela.mainloop()
    def tela(self):
       #TITULO PRINCIPAL DO PROGRAMA
       self.janela.title("Simulador De Bancas")
       #plano de fundo do programa pode ser uma foto ou uma cor.
       self.janela.configure(background= "#A9A9A9")
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
       self.frame1 = Frame (self.janela, bd= 3, bg="#F57C00", highlightthickness=10, highlightbackground="#2F4F4F")
       self.frame1.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
    #cria uma label aonde sera exibida o valor da banca e atualizado.
    def _banca(self):
       self.label_banca = Label(self.frame1, text=f"Banca: R$ {self.banca:.2f}",bg="#F57C00",fg="white",font=('arial', 35,'bold') )
       self.label_banca.place(relx=0.25, rely=0.01)
    #criar botao editar banca, aonde ele ira editar saldo da banca.
    def botao_banca(self):
       self.botao_editar = Button(self.frame1, text="Editar Banca", font=("Arial", 20), command=self.ativar_edicao)
       self.botao_editar.place(relx=0.05, rely=0.15)
    # função do botao que ira ativar edição
    def ativar_edicao(self):
       #ao apertar no botao ele esconde o botao
       self.botao_editar.place_forget ()

       #entrada do valor da banca

       self.valor_banca = Entry(self.frame1, font=('arial', 20))
       self.valor_banca.place(relx=0.05, rely=0.15)
        # o valor da banca atual
       self.valor_banca.insert(0, str(self.banca))

       # Botão para confirmar a alteração da banca
       self.botao_confirmar = Button(self.frame1, text="Confirmar", font=("Arial", 14), command=self.atualizar_banca)
       self.botao_confirmar.place(relx=0.05, rely=0.2)

        #atualizar banca 
    def atualizar_banca(self):
       """"Coloque Um Valor Para Atualizar Banca"""
       try:
          #pega valor insirido pelo user
          valor = float(self.valor_banca.get())
          #atualiza o valor da banca
          self.banca = valor

          #atualiza a label da banca para mostrar o valor exato da banca
          self.label_banca.config(text=f"Banca: R$ {self.banca:.2f}")

          #limpa o campo de entrada e os botao

          self.valor_banca.place_forget()
          self.botao_confirmar.place_forget()

          # ira exibir novamente o botao editar
          self.botao_editar.place(relx=0.05, rely=0.15)

        #se valor nao for numero ira exibir um erro
       except ValueError:
          erro_banca = Label(self.frame1, text="Escreva apneas numeros!!", font=('arial', 20), fg='RED',  bg="#F57C00")
          erro_banca.place(relx=0.05, rely=0.25)
          self.janela.after(2000, erro_banca.place_forget) # remove o erro apos 2 segundos

Applicação()