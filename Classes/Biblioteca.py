from Classes.Livro import Livro
from Utils.jsonHandler import carregarDadosDatabase, salvarDadosDatabase, criadorJsonDatabase

class Biblioteca:

    def __init__(self, nomeBiblioteca:str):
        self.nomeBiblioteca = nomeBiblioteca
        criadorJsonDatabase()
        self.livrosDb = carregarDadosDatabase()

    def adicionarLivro(self, livro:Livro):
        
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


    def removerLivro(self, titulo:str):
        livros = self.livrosDb["Livros"]
        for i, livro in enumerate(livros):
            if livro["Titulo"] == titulo:
                del livros[i]
                salvarDadosDatabase(self.livrosDb)

    
    def buscarLivro(self, titulo:str) -> Livro:
        livros = self.livrosDb["Livros"]
        for livro in livros:
            if livro["Titulo"] == titulo:
                return livro
    
        return None
            

    def alterarDisponibilidade(self, tituloLivro:str):
        livros = self.livrosDb["Livros"]
        for livro in livros:
            if livro["Titulo"] == tituloLivro:
                
                if livro["Disponivel"]:
                    livro["Disponivel"] = False
                else:
                    livro["Disponivel"] = True
        salvarDadosDatabase(self.livrosDb)


    def verificarDisponibilidade(self, tituloLivro:str):
        livros = self.livrosDb["Livros"]
        for livro in livros:
            if livro["Titulo"] == tituloLivro:
                if livro["Disponivel"]:
                    return True
                else:
                    return False