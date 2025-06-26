from Classes.Biblioteca import Biblioteca
from Classes.Autenticador import Autenticador

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
            case "4":
                main()

def fluxoMenusBibliotecario():
    while True:
        menu.menuInicialBibliotecario()
        match str(input()):
            case "1":
                fluxo.fluxoAdicionarLivro(biblioteca=bibliotecaObj)
            case "2":
                fluxo.fluxoRetirarLivro(biblioteca=bibliotecaObj)
            case "3":
                fluxo.fluxoBuscarLivro(biblioteca=bibliotecaObj)
            case "4":
                fluxo.fluxoListarLivros(biblioteca=bibliotecaObj)
            case "5":
                fluxo.fluxoTornarBibliotecario(autenticador=autenticador)
            case "6":
                main()


def main():
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



#Cria a instancia do Autenticador
autenticador = Autenticador()

#Cria a instancia da Biblioteca
bibliotecaObj = Biblioteca()


main()

