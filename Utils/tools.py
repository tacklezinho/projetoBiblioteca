from Classes.Biblioteca import Biblioteca
from Classes.Livro import Livro


def livroExiste(titulo : str, biblioteca : Biblioteca) -> bool:
    livros = biblioteca.livrosDb["Livros"]
    for livroInDb in livros:
        if livroInDb["Titulo"] == titulo:
            return True
    return False


def alterarDisponibilidade(biblioteca:Biblioteca):
    pass
