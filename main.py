from Classes.Livro import Livro
from Classes.Biblioteca import Biblioteca
from Utils.funcoes_tools import *
import Utils.menus_utils as menu
import Utils.fluxos_menus as fluxo



#Cria a instancia da Biblioteca
bibliotecaObj = Biblioteca(nomeBiblioteca=input("Digite o nome da sua biblioteca: "))

#Adiciona um livro inicial para Debug
bibliotecaObj.adicionarLivro(Livro(titulo="Livro Teste", autor="Autor Teste"))

while True:
    menu.menuInicial()
    match input():
        case "1":
            fluxo.fluxoAdicionarLivro(bibliotecaObj, menu)
        case "2":
            fluxo.fluxoRetirarLivro(bibliotecaObj, menu)
        case "3":
            fluxo.fluxoBuscarLivro(bibliotecaObj, menu)
        case "4":
            fluxo.fluxoListarLivros(bibliotecaObj, menu)