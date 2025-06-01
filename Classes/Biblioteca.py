from Classes.Livro import Livro

class Biblioteca:

    def __init__(self, nomeBiblioteca):
        self.nomeBiblioteca = nomeBiblioteca
        self.livrosDb = []

    def adicionarLivro(self, livro):
        if isinstance(livro, Livro):
            self.livrosDb.append(livro)
            print("\nLivro Adicionado Com Sucesso!")
        else:
            print("\nAdicione apenas objetos do tipo Livro")

    def listarLivros(self):
        for livro in self.livrosDb:
            print(livro)
