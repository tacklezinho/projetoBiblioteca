from Utils.jsonHandler import sessaoAtual, carregarSessaoAtual

class Usuario:
    

    def __init__(self, nomeUsuario:str, senhaUsuario:str, bibliotecario=False, livrosPossuidos=[]):
        self.nomeUsuario = nomeUsuario
        self.senhaUsuario = senhaUsuario
        self.bibliotecario = bibliotecario
        self.livrosPossuidos = livrosPossuidos


    def emprestarLivro(self, livro:dict) -> None:
        livroDict = {"Titulo":livro["Titulo"], "Autor":livro["Autor"]}
        self.livrosPossuidos.append(livroDict)
        sessaoAtual(self.toDict())

    def devolverLivro(self, tituloLivro:str) -> bool:
        for contador, livro in enumerate(self.livrosPossuidos):
            if livro["Titulo"] == tituloLivro:
                del self.livrosPossuidos[contador]
                sessaoAtual(self.toDict())
                return True
        return False


    def toDict(self) -> dict:
        userDict = {
            "User": self.nomeUsuario,
            "Password": self.senhaUsuario,
            "AdminAcess": self.bibliotecario,
            "LivrosPossuidos": self.livrosPossuidos
            }
        return userDict
    
    def listarLivrosPessoais(self) -> None:
        print("\n-- Livros Possuidos --")
        for livro in self.livrosPossuidos:
            print("-----------------")
            print("Título: ", livro["Titulo"])
            print("Autor: ", livro["Autor"])
            print("-----------------")