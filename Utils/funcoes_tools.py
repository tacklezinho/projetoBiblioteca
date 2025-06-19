from Classes.Biblioteca import Biblioteca
from Classes.Livro import Livro


def livroJaExiste(livro : Livro, biblioteca : Biblioteca) -> bool:
    for livroInDb in biblioteca.livrosDb:
        if livro.titulo == livroInDb.titulo:
            return True
    return False


def getLivroByTitle(titulo:str, biblioteca:Biblioteca) -> None:
    for livro in biblioteca.livrosDb:
        if livro.titulo == titulo:
            return livro
    return "Livro Não Encontrado!"





def getIndexByTitle(titulo:str, livrosDb:list)-> int:
    contador = 0
    for livro in livrosDb:
        if livro.titulo == titulo:
            return contador
        else:
            contador += 1

def retiraLivroPorTitulo(titulo, biblioteca:Biblioteca)-> None:
    indexLivro = getIndexByTitle(titulo=titulo, livrosDb=biblioteca.livrosDb)
    if indexLivro == None:
        print("\nLivro não encontrado!")
    else:
        biblioteca.livrosDb.pop(indexLivro)
        print("\nLivro Retirado Com Sucesso!")