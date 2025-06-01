from Classes.Biblioteca import Biblioteca
from Classes.Livro import Livro


def livroJaExiste(livro : Livro, biblioteca : Biblioteca) -> bool:
    for livroInDb in biblioteca.livrosDb:
        if livro.titulo == livroInDb.titulo:
            return True
    return False


def getIndexByTitle(titulo:str, livrosDb:list)-> int:
    contador = 0
    for livro in livrosDb:
        if livro.titulo == titulo:
            return contador
        else:
            contador += 1

def retiraLivroPorTitulo(titulo, biblioteca:Biblioteca)-> None:
    indexLivro = getIndexByTitle(titulo=titulo, livrosDb=biblioteca.livrosDb)
    biblioteca.livrosDb.pop(indexLivro)
    print("Livro Retirado Com Sucesso!")