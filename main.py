from Classes.Livro import Livro
from Classes.Biblioteca import Biblioteca
from Classes.Autenticador import Autenticador
from Utils.tools import *
import Utils.simpleMenus as menu
import Utils.fluxoMenus as fluxo
import Utils.fluxoLoginCadastro as logCad


def fluxoMenusUsuario(usuarioAtual):
    while True:
        menu.menuInicialUsuario()
        match str(input()):
            case "1":
                fluxo.fluxoEmprestarLivro(usuarioAtual=usuarioAtual, biblioteca=bibliotecaObj, autenticador=autenticador)
            case "2":
                pass
            case "3":
                pass

def fluxoMenusBibliotecario():
    menu.menuInicialBibliotecario()






autenticador = Autenticador()

#Cria a instancia da Biblioteca
bibliotecaObj = Biblioteca(nomeBiblioteca=input("Digite o nome da sua biblioteca: "))


while True:
    menu.menuLoginOuCadastro()
    match input():
        case "1":
            if logCad.fluxoLoginUsuario(autenticador):
                usuarioAtual = logCad.getSessaoAtual()
                if usuarioAtual.bibliotecario:
                    fluxoMenusBibliotecario()
                else:
                    fluxoMenusUsuario(usuarioAtual)
                break
        case "2":
            logCad.fluxoCadastroUsuario(autenticador)

