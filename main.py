import tkinter as tk
import prova as prov

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.ProvaMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)

        self.ProvaMenu.add_command(label="caixa1", command=self.controle.caixaUm)
        self.ProvaMenu.add_command(label="caixa2", command=self.controle.caixaDois)
        self.ProvaMenu.add_command(label="caixa3", command=self.controle.caixaTres)
        self.menubar.add_cascade(label="Prova", menu=self.ProvaMenu)
               
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProva = prov.CtrlProva()

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Prova 2")
        # Inicia o mainloop
        self.root.mainloop()
    
    def caixaUm(self):
        self.ctrlProva.caixaUm()
    
    def caixaDois(self):
        self.ctrlProva.caixaDois()

    def caixaTres(self):
        self.ctrlProva.caixaTres()

if __name__ == '__main__':
    c = ControlePrincipal()