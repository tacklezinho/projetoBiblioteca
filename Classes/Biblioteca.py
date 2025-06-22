from Classes.Livro import Livro
from Utils.json_handler import carregarDadosDatabase, salvarDadosDatabase, criadorJsonDatabase

class Biblioteca:

    def __init__(self, nomeBiblioteca):
        self.nomeBiblioteca = nomeBiblioteca
        criadorJsonDatabase()
        self.livrosDb = carregarDadosDatabase()

    def adicionarLivro(self, livro):
        
        if isinstance(livro, Livro):
            livroDict = {"Titulo":livro.titulo, "Autor":livro.autor, "Disponivel":livro.disponivel}
            self.livrosDb["Livros"].append(livroDict)
            salvarDadosDatabase(livrosDatabase=self.livrosDb)
            print("\nLivro Adicionado Com Sucesso!")
        
        else:
            print("\nAdicione apenas objetos do tipo Livro")


    def listarLivros(self):
        livros = self.livrosDb["Livros"]
        for livro in livros:
            print("\n----------------")
            print("Titulo: ", livro["Titulo"])
            print("Autor: ", livro["Autor"])
            print("Disponivel: ", livro["Disponivel"])
            print("----------------")


    def removerLivro(self, titulo):
        livros = self.livrosDb["Livros"]
        for i, livro in enumerate(livros):
            if livro["Titulo"] == titulo:
                del livros[i]
                salvarDadosDatabase(self.livrosDb)