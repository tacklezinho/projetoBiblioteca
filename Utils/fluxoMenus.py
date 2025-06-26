from types import ModuleType
from Classes.Livro import Livro
from Classes.Biblioteca import Biblioteca
from Utils.tools import livroExiste
from Classes.Usuario import Usuario



def fluxoAdicionarLivro(biblioteca : Biblioteca, menu : ModuleType) -> None:
    tituloLivro = str(input("Digite o titulo do livro: "))
    autorLivro = str(input("Digite o autor do livro: "))
    livro = Livro(titulo=tituloLivro, autor=autorLivro)
    if livroExiste(titulo=tituloLivro, biblioteca=biblioteca):
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

def fluxoListarLivros(biblioteca : Biblioteca, menu : ModuleType) -> None:
    biblioteca.listarLivros()

def fluxoEmprestarLivro(usuarioAtual:Usuario, biblioteca:Biblioteca, autenticador):
        tituloLivro = str(input("Digite o titulo que deseja retirar: "))
        livro = biblioteca.buscarLivro(titulo=tituloLivro)
        if livro == None:
            print("\nLivro não encontrado!")
        else:
            if biblioteca.verificarDisponibilidade(livro["Titulo"]):
                usuarioAtual.emprestarLivro(livro=livro)
                biblioteca.alterarDisponibilidade(livro["Titulo"])
                autenticador.atualizarUsuarios(usuarioAtual.toDict())