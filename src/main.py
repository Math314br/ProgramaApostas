#aqui é o programa pricincipal aonde tudo ira rodar.
from tkinter import *
from tkinter import ttk
import json
import os
import re


janela = Tk()

class Applicação():
    def __init__(self):
     self.janela= janela
     self.banca = 100 # valor da banca inicial
     self.tela()
     self.frameTELA()
     self._banca()
     self.botao_banca()
     self.carregar()
     self.ativar_edicao()
     self.atualizar_banca()
     self.aposta()
     self.valor_aposta()
     self.valor_odd()
     self.green()
     self.red()
     self.frame2()
     self.historico()
     self.salvar_aposta(resultado=0)
     self.salvar()
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
       self.label_banca = Label(self.frame1, text=f"Banca: R$ {self.banca:.2f}",bg="#F57C00",fg="white",font=('arial', 30,'bold') )
       self.label_banca.place(relx=0.25, rely=0.01)

    #criar botao editar banca, aonde ele ira editar saldo da banca.

    def botao_banca(self):
       self.botao_editar = Button(self.frame1, text="Editar Banca", font=("Arial", 13), command=self.ativar_edicao)
       self.botao_editar.place(relx=0.25, rely=0.01)

    # função do botao que ira ativar edição

    def ativar_edicao(self):
       #ao apertar no botao ele esconde o botao
       self.botao_editar.place_forget ()

       #entrada do valor da banca

       self.valor_banca = Entry(self.frame1, font=('arial', 30))
       self.valor_banca.place(relx=0.25, rely=0.01)
        # o valor da banca atual
       self.valor_banca.insert(0, str(self.banca))

       # Botão para confirmar a alteração da banca
       self.botao_confirmar = Button(self.frame1, text="Confirmar", font=("Arial", 15), command=self.atualizar_banca)
       self.botao_confirmar.place(relx=0.04, rely=0.01)

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
          self.botao_editar.place(relx=0.04, rely=0.01)

        #se valor nao for numero ira exibir um erro
       except ValueError:
          erro_banca = Label(self.frame1, text="Escreva apneas numeros!!", font=('arial', 20), fg='RED',  bg="#F57C00")
          erro_banca.place(relx=0.05, rely=0.25)
          self.janela.after(2000, erro_banca.place_forget) # remove o erro apos 2 segundos
     # APOSTA COM VALORES DA ODD E APOSTA
    def aposta(self):
       #label aposta
       self.label_aposta = Label(self.frame1, text="APOSTA", font=('arial', 30))
       self.label_aposta.place(relx=0.36, rely=0.08)
    def valor_aposta(self):
       self.label_valor = Label(self.frame1, text="Valor Da Aposta:", font=('arial',25))
       self.label_valor.place(relx=0.04, rely=0.14)
       # ENTRADA
       self.entry_valor = Entry(self.frame1, text="Valor Da Aposta:", font=('arial',18))
       self.entry_valor.place(relx=0.04, rely=0.19)



    def valor_odd(self):
        self.label_odd = Label(self.frame1, text="Valor Da ODD:", font=('arial', 25))
        self.label_odd.place(relx=0.54, rely=0.14)
        
        # Campo de entrada para a odd
        self.entry_odd = Entry(self.frame1, font=('arial', 18))
        self.entry_odd.place(relx=0.54, rely=0.19)



       

    # BOTAO GRENN E RED
    def green(self):
       self.botao_green = Button(self.frame1,text="GREEN", font=('arial',30,'bold'), command=lambda: self.salvar_aposta("GREEN"))
       self.botao_green.place(relx=0.16, rely=0.24)
    def red(self):
       self.botao_red = Button(self.frame1,text="RED", font=('arial',30,'bold'),command=lambda: self.salvar_aposta("RED"))
       self.botao_red.place(relx=0.56, rely=0.24)
      


     ### FRAME 2 PARA TELA DE HISTORICO
    def frame2(self):
       self.frame2 = Frame (self.janela, bd= 3, bg="#F57C00", highlightthickness=10, highlightbackground="#2F4F4F")
       self.frame2.place(relx=0.025, rely=0.34, relwidth=0.95, relheight=0.95) 

   ### criaçaão do historico e tabelas
    def historico(self):
       ## TITULO DO HISTORICO
       self.nomehistorico = Label(self.frame2, text="HISTORICO", font=('arial', 30, 'bold'))
       self.nomehistorico.place(relx=0.30, rely=0.01)
       ## sao colunas da tabela sao 3 uma para odd,valor da posta e o resultado.
       self.hisotricotabela = ttk.Treeview(self.frame2, height=3,
                                           column=("col1","col2","col3"))
       ## cabeçalho da coluna
       self.hisotricotabela.heading("#0", text="ODD")
       self.hisotricotabela.heading("#1", text="VALOR")
       self.hisotricotabela.heading("#2", text="RESULTADO")
       ## tamanho da coluna na tela
       self.hisotricotabela.column("#0", width=15)
       self.hisotricotabela.column("#1", width=50)
       self.hisotricotabela.column("#2", width=20)

       self.hisotricotabela.place(relx=0.05, rely=0.07, relheight=0.50,relwidth=0.90)

    def salvar_aposta(self,resultado):
       try:
         odd = float(self.entry_odd.get())
         valor = float(self.entry_valor.get())

         #ver se aposta maior que banca.

         if valor > self.banca:
            banca_menor = Label(self.frame1, text="SALDO INSUFICIENTE !",font=('arial', 20), fg='RED', bg="#F57C00")
            banca_menor.place(relx=0.05, rely=0.30)
            self.janela.after(2000,banca_menor.place_forget) #some mensagem
            return
         
         #calcular resultado das apostas
         if resultado == "GREEN":
            lucro = valor * (odd - 1)
            self.banca += lucro
         elif resultado == "RED":
            self.banca -= valor
         
         # atualizar interface da banca
         self.label_banca.config(text=f"Banca: R$ {self.banca:.2f}")

         #salvar no historico 
         self.hisotricotabela.insert("","end", values=(odd,valor,resultado))
         self.salvar()
       except ValueError:
           erro_valor = Label(self.frame1, text="Digite apenas numeros!",font=('arial', 20), fg='RED', bg="#F57C00")
           erro_valor.place(relx=0.05, rely=0.30)
           self.janela.after(2000, erro_valor.place_forget)








    def salvar(self):
       #salvar historico local
       historico  = []
       for item in self.hisotricotabela.get_children():
          valores = self.hisotricotabela.item(item,'values')
          historico.append(valores)

       #criar historico
       dados = {
         "banca": self.banca,
         "historico": historico}
       with open('historico.json','w') as arquivo:
          json.dump(historico, arquivo, indent=4)
          print("historico salvo com sucesso!!")

    def carregar(self):
       if os.path.exists("historico.json"):
          with open("historico.json", 'r') as  arquivo:
             try:
                dados = json.load(arquivo)
                #corrigindo se for lista
                if isinstance(dados, list):
                  dados =  {"banca": 100,  "historico": []}

                # restaurar a a banca
                self.banca = dados.get("banca",[])
                self.label_banca.config(text=f"banca: R$ {self.banca:.2f}")

                #restaurar historico
                historico = dados.get("historico", [])
                for valores in historico:
                  self.hisotricotabela.insert("","end", values=valores)
                
             except json.JSONDecodeError:
                pass
       
   

Applicação()