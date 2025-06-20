class Livro:
    def __init__(self, titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nDisponivel: {self.disponivel}"
    
    def __eq__(self, outro):
        return isinstance(outro, Livro) and self.titulo == outro.titulo