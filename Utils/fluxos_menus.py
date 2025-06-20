from types import ModuleType
from Classes.Livro import Livro
from Classes.Biblioteca import Biblioteca
from Utils.funcoes_tools import livroJaExiste, retiraLivroPorTitulo, getLivroByTitle



def fluxoAdicionarLivro(biblioteca : Biblioteca, menu : ModuleType) -> None:
    tituloLivro = str(input("Digite o titulo do livro: "))
    autorLivro = str(input("Digite o autor do livro: "))
    livro = Livro(titulo=tituloLivro, autor=autorLivro)
    if livroJaExiste(livro=livro, biblioteca=biblioteca):
        print("\n--- Esse livro que está tentando adicionar já existe ---\n")
    else:
        biblioteca.adicionarLivro(livro=livro)

def fluxoRetirarLivro(biblioteca : Biblioteca, menu : ModuleType) -> None:
    tituloLivro = str(input("Digite o titulo que deseja retirar: "))
    retiraLivroPorTitulo(titulo=tituloLivro, biblioteca=biblioteca)

def fluxoBuscarLivro(biblioteca : Biblioteca, menu : ModuleType) -> None:
    tituloLivro = str(input("Digite o titulo que deseja buscar: "))
    print("\n", getLivroByTitle(titulo=tituloLivro, biblioteca=biblioteca))
    

def fluxoListarLivros(biblioteca : Biblioteca, menu : ModuleType) -> None:
    for livro in biblioteca.livrosDb:
        print("-------------------")
        print(livro)
        print("-------------------")
    print("\n")

