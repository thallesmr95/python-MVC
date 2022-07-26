import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco, avaliacao):
        self.codigo = codigo
        self.titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco
        self.avaliacao = avaliacao
    
    def getCodigo(self):
        return self.codigo

    def getTitulo(self):
        return self.titulo

    def getConsole(self):
        return self.console

    def getGenero(self):
        return self.genero

    def getPreco(self):
        return self.preco

    def getAvaliacao(self):
        return self.avaliacao

    def appendAvaliacao(self, value):
        return self.avaliacao.append(value)

    def getEstrela(self) -> int:
        if len(self.avaliacao) == 0: 
            return 0 

        media = sum(self.avaliacao) / len(self.avaliacao)
        estrela = 0
        
        return estrela

    def getJogo(self):

        return "Título: " + str(self.getTitulo())\
        + "\nCodigo: " + str(self.getCodigo())\
        + "\nConsole: " + str(self.getConsole())\
        + "\nGênero: " + str(self.getGenero())\
        + "\nPreço: " + str(self.getPreco())\
        + "\nAvaliação: " + str(self.getEstrela())


class consoleInv(Exception):
    pass

class generoInv(Exception):
    pass

class campoVazio(Exception):
    pass
    

class LimiteInsereJogo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('260x200')
        self.title("Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()

      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelTitulo = tk.Label(self.frameTitulo,text="Título:   ")
        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero, text="Gênero: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco:   ")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")


        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputConsole = tk.Entry(self.frameConsole, width=20)
        self.inputGenero = tk.Entry(self.frameGenero, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputCodigo.pack(side="left")
        self.inputTitulo.pack(side="left")
        self.inputConsole.pack(side="left")
        self.inputGenero.pack(side="left")
        self.inputPreco.pack(side="left")

      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left", pady=10)
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left", pady=10)
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left", pady=10)
        self.buttonFecha.bind("<Button>", controle.fechaHandler)


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaJogo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)

        self.geometry('400x250')
        self.title("Consultar Jogos")

        self.ctrl = controle

        self.consoles = []
        self.generos = []

        for jogo in self.ctrl.listaJogos:

            if(not jogo.getConsole() in self.consoles):
                self.consoles.append(jogo.getConsole())
            if(not jogo.getGenero() in self.generos):
                self.generos.append(jogo.getGenero())

        self.frameCombos = tk.Frame(self)
        self.frameCombos.pack(pady=3)

        self.labelConsoles = tk.Label(self.frameCombos,text="Consoles: ")
        self.labelConsoles.pack(side="left")
        self.escolhaConsole = tk.StringVar()
        self.comboboxConsole = ttk.Combobox(self.frameCombos, width = 15 ,values=self.consoles, textvariable = self.escolhaConsole)
        self.comboboxConsole.pack(side="left")
        self.comboboxConsole.bind("<<ComboboxSelected>>", self.ctrl.exibeConsole)

        self.labelGenero = tk.Label(self.frameCombos,text="Gêneros: ")
        self.labelGenero.pack(side="left")
        self.escolhaGenero = tk.StringVar()
        self.comboboxGenero = ttk.Combobox(self.frameCombos, width = 15 ,values=self.generos, textvariable = self.escolhaGenero)
        self.comboboxGenero.pack(side="left")
        self.comboboxGenero.bind("<<ComboboxSelected>>", self.ctrl.exibeGenero)

        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, height=20,width=40)
        self.textJogos.pack()
        self.textJogos.config(state=tk.DISABLED)



class LimiteAvaliaJogo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)

        self.geometry('400x250')
        self.title("Avaliar Jogos")
        self.ctrl = controle

        self.titulos = []

        for jogo in self.ctrl.listaJogos:
            if(not jogo.getTitulo() in self.titulos):
                self.titulos.append(jogo.getTitulo())

        self.frameCombos = tk.Frame(self)
        self.frameCombos.pack(pady=3)

        self.labelTitulos = tk.Label(self.frameCombos,text="Títulos: ")
        self.labelTitulos.pack(side="left")
        self.escolhaTitulo = tk.StringVar()
        self.comboboxTitulo = ttk.Combobox(self.frameCombos, width = 15 ,values=self.titulos, textvariable = self.escolhaTitulo)
        self.comboboxTitulo.pack(side="left")
        self.comboboxTitulo.bind("<<ComboboxSelected>>", self.ctrl.exibeTitulo)

        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, height=25,width=45)
        self.textJogos.pack()
        self.textJogos.config(state=tk.DISABLED)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Avaliar")      
        self.buttonSubmit.pack(side="left", pady=10)
        self.buttonSubmit.bind("<Button>", controle.enterHandler) 

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left", pady=10)
        self.buttonFecha.bind("<Button>", controle.fechaHandler)



class CtrlJogo():
    def __init__(self, controlador):
        self.controlador = controlador

        self.listaConsoles = ["XBox", "PlayStation", "Switch", "PC"]

        self.listaGen = ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]

        self.listaJogos =  []
    
    def cadastraJogo(self):
        self.limiteIns = LimiteInsereJogo(self)

    def consultaJogo(self):
        self.limiteCons = LimiteConsultaJogo(self)

    def avaliaJogo(self):
        self.limiteCons = LimiteAvaliaJogo(self)
    
    def enterHandler(self, event):

        # Recebe as entradas e as verifica

        codigo = self.limiteIns.inputCodigo.get()
        titulo = self.limiteIns.inputTitulo.get()
        console = self.limiteIns.inputConsole.get()
        genero = self.limiteIns.inputGenero.get()
        preco = self.limiteIns.inputPreco.get()

        try:
            if codigo == '' or titulo == '' or console == '' or genero == '' or preco == '':
                raise campoVazio()
            elif console not in self.listaConsoles:
                raise consoleInv()
            elif genero not in self.listaGen:
                raise generoInv()

        except consoleInv:
            self.limiteIns.mostraJanela('Erro!', 'Console inválido')
        except generoInv:
            self.limiteIns.mostraJanela('Erro!', 'Gênero inválido\n')
        except campoVazio:
            self.limiteIns.mostraJanela('Erro!', 'Não é permitido deixar campos vazios')
        else:            
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.listaJogos.append(jogo)            
            self.limiteIns.mostraJanela('Sucesso!', 'Jogo cadastrado')
            self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputConsole.delete(0, len(self.limiteIns.inputConsole.get()))
        self.limiteIns.inputGenero.delete(0, len(self.limiteIns.inputGenero.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeConsole(self,event):
        consoleSel = self.limiteCons.comboboxConsole.get()
        self.limiteCons.comboboxGenero.set("----")
        self.limiteCons.textJogos.config(state='normal')
        self.limiteCons.textJogos.delete("1.0", tk.END)

        for jogo in self.listaJogos:
            if(jogo.getConsole() == consoleSel):
                jogoSel = jogo.getJogo() + "\n\n"
                self.limiteCons.textJogos.insert(1.0, jogoSel)
        self.limiteCons.textJogos.config(state='disable')

    def exibeGenero(self, event):
        self.limiteCons.comboboxConsole.set("----")
        generoSel = self.limiteCons.comboboxGenero.get()
        self.limiteCons.textJogos.config(state='normal')
        self.limiteCons.textJogos.delete("1.0", tk.END)

        for jogo in self.listas:

            if(jogo.getGenero() == generoSel):
                jogoSel = jogo.getJogo() + "\n\n"
                self.limiteCons.textJogos.insert(1.0, jogoSel)
        self.limiteCons.textJogos.config(state='disable')


    def exibeTitulo(self,event):
        tituloSel = self.limiteCons.comboboxTitulo.get()
        self.limiteCons.comboboxGenero.set("----")
        self.limiteCons.textJogos.config(state='normal')
        self.limiteCons.textJogos.delete("1.0", tk.END)
        
        for jogo in self.listas:
            if(jogo.getTitulo() == tituloSel):
                jogoSel = jogo.getJogo() + "\n\n"
                self.limiteCons.textJogos.insert(1.0, jogoSel)
        self.limiteCons.textJogos.config(state='disable')


