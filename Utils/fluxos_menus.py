from types import ModuleType
from Classes.Livro import Livro
from Classes.Biblioteca import Biblioteca
from Utils.funcoes_tools import livroExiste, getLivroByTitle



def fluxoAdicionarLivro(biblioteca : Biblioteca, menu : ModuleType) -> None:
    tituloLivro = str(input("Digite o titulo do livro: "))
    autorLivro = str(input("Digite o autor do livro: "))
    livro = Livro(titulo=tituloLivro, autor=autorLivro)
    if livroExiste(titulo=tituloLivro):
        print("\n--- Esse livro que está tentando adicionar já existe ---\n")
    else:
        biblioteca.adicionarLivro(livro=livro)

def fluxoRetirarLivro(biblioteca : Biblioteca, menu : ModuleType) -> None:
    tituloLivro = str(input("Digite o titulo que deseja retirar: "))
    if livroExiste(titulo=tituloLivro, biblioteca=biblioteca):
        biblioteca.removerLivro(titulo=tituloLivro)
        print("\nLivro removido com sucesso!")
    else:
        print("\n--- Livro não encontrado! ---\n")

def fluxoBuscarLivro(biblioteca : Biblioteca, menu : ModuleType) -> None:
    tituloLivro = str(input("Digite o titulo que deseja buscar: "))
    print("\n", getLivroByTitle(titulo=tituloLivro, biblioteca=biblioteca))
    

def fluxoListarLivros(biblioteca : Biblioteca, menu : ModuleType) -> None:
    biblioteca.listarLivros()