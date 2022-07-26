import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Classes do Menu

class Curso:
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

class Est:
    def __init__(self, nro, nome, curso):
        self.__nro = nro
        self.__nome = nome
        self.__curso = curso

    def getNro(self):
        return self.__nro

    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso

# Classe Principal

class Prova:
    def __init__(self, curso, listaEstEquipe):
        self.__curso = curso
        self.__listaEstEquipe = listaEstEquipe

    def getCurso(self):
        return self.__curso

    def getListaEstEquipe(self):
        return self.__listaEstEquipe


# Inserção 

class LimiteInsereEquipe(tk.Toplevel):
    def __init__(self, controle, listaCodigoCurso):

        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Prova")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameNro = tk.Frame(self)
        #self.frameOpc = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCurso.pack()
        self.frameNro.pack()
        #self.frameOpc.pack()
        self.frameButton.pack()        

        self.labelDiscip = tk.Label(self.frameCurso,text="Curso: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodigoCurso
          
        self.labelNro = tk.Label(self.frameNro,text="Nro: ")
        self.labelNro.pack(side="left")
        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")

        #self.labelOpc = tk.Label(self.frameOpc,text="opção: ")
        #self.labelOpc.pack(side="left")
        #self.inputOpc = tk.Entry(self.frameOpc, width=20)
        #self.inputOpc.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Estudante")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereEstudante)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Equipe")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaEquipe)   

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaEquipe(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Prova")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCurso.pack()
        self.frameButton.pack()        
          
        self.labelCurso = tk.Label(self.frameCurso,text="Código do curso: ")
        self.labelCurso.pack(side="left")
        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")

        self.buttonConsulta = tk.Button(self.frameButton ,text="Consulta")           
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controle.consultaCodigo)   

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlProva():       
    def __init__(self):
        self.listaEquipes = []

        c1 = Curso("CCO", "Ciência da Computação")
        c2 = Curso("SIN", "Sistemas de Informação")
        c3 = Curso("EEL", "Engenharia Elétrica")
        self.listaC = []
        self.listaC.append(c1)
        self.listaC.append(c2)
        self.listaC.append(c3)
        #Inserir mais cursos, se quiser

        self.listaE = []
        self.listaE.append(Est(1001, "José", c1))
        self.listaE.append(Est(1002, "João", c1))
        self.listaE.append(Est(1003, "Rui", c2))  
        self.listaE.append(Est(1004, "Marina", c2))
        self.listaE.append(Est(1005, "Pedro", c3))            

    #Primeira caixa do Menu Controlador
    
    def caixaUm(self):        
        self.listaEstEquipe = []
        listaCodigoCurso = []

        for curso in self.listaC:
            listaCodigoCurso.append(curso.getCodigo())
        self.limiteIns = LimiteInsereEquipe(self, listaCodigoCurso)

    
    # Regras de Negócio para a definição da criação

    def criaEquipe(self, event):
        if not self.listaEstEquipe:
            self.limiteIns.mostraJanela('Erro', 'Não é permitido criar equipe sem estudantes')
            return

        codigoSel = self.limiteIns.escolhaCombo.get()
        print(codigoSel)

        for curso in self.listaCurso:
            if curso.getCodigo() == codigoSel:
                break

        equipe = Prova(curso, self.listaEstEquipe)
        self.listaEquipes.append(equipe)
        self.limiteIns.mostraJanela('Sucesso', 'Equipe criada com sucesso')
        self.limiteIns.destroy()

    #Definição para inserir uma classe dentro do Menu

    def insereEstudante(self, event):

        codigoSel = self.limiteIns.escolhaCombo.get()

        for curso in self.listaC:
            if curso.getCodigo() == codigoSel:
                break

        nroInput = int(self.limiteIns.inputNro.get())
        estudante = None

        for est in self.listaE:
            if est.getNro() == nroInput:
                estudante = est
                break

        if estudante is None:
            self.limiteIns.mostraJanela('Erro', 'Nro de matrícula não existe')
            self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
            return

        if estudante.getCurso() != curso:
            self.limiteIns.mostraJanela('Erro', 'Estudante não faz parte do curso')
            self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
            return

        self.listaEstEquipe.append(estudante)
        self.limiteIns.mostraJanela('Sucesso', 'Estrudante inserido na equipe') 
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))                   


    # Segunda Caixa Do Menu Controlador
    
    def caixaDois(self):
        self.limiteCons = LimiteConsultaEquipe(self)

    def consultaCodigo(self, event):
        codigoInput = self.limiteCons.inputCurso.get()
        curso = None

        for cur in self.listaC:
            if cur.getCodigo() == codigoInput:
                curso = cur
                break  

        if curso is None:
            self.limiteCons.mostraJanela('Erro', 'Este curso não existe') 
            self.limiteCons.inputCurso.delete(0, len(self.limiteCons.inputCurso.get()))
            return
        achou = False

        for equipe in self.listaEquipes:
            if equipe.getCurso() == curso:
                achou = True
                break

        if not achou:
            self.limiteCons.mostraJanela('Erro', 'Este curso não possui equipe') 
            self.limiteCons.inputCurso.delete(0, len(self.limiteCons.inputCurso.get()))
            return

        str = ''
        str += 'Curso: ' + curso.getNome() + '\n'
        str += 'Estudantes:\n'
        for estud in equipe.getListaEstEquipe():
            str += estud.getNome() + '\n'
        self.limiteCons.mostraJanela('Equipe', str)                   


#   Terceira Caixa Do Menu Controlador

    def caixaTres(self):
        contEq = len(self.listaEquipes)
        contEst = 0
        for equipe in self.listaEquipes:
            contEst += len(equipe.getListaEstEquipe())
        mediaEq = contEst/contEq
        strg = "Número de equipes: " + str(contEq) + "\n"
        strg += "Número total de estudantes: " + str(contEst) + "\n"
        strg += "Média de estudantes por equipe: " + str(mediaEq)
        messagebox.showinfo("Dados do campeonato", strg)        

