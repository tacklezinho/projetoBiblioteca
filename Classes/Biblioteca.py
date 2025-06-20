from Classes.Livro import Livro
import json

class Biblioteca:

    def __init__(self, nomeBiblioteca):
        self.nomeBiblioteca = nomeBiblioteca
        self.livrosDb = {"Livros":[]}

    def adicionarLivro(self, livro):
        
        if isinstance(livro, Livro):
            livroDict = {"Titulo":livro.titulo, "Autor":livro.autor, "Disponivel":livro.disponivel}
            self.livrosDb["Livros"].append(livroDict)
            
            with open(r"Database/livros.json", "w") as f:        
                json.dump(self.livrosDb, f, indent=2)
            print("\nLivro Adicionado Com Sucesso!")
        
        else:
            print("\nAdicione apenas objetos do tipo Livro")


    def listarLivros(self):
        for livro in self.livrosDb:
            print(livro)
