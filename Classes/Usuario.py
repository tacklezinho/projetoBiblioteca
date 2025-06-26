from Utils.jsonHandler import sessaoAtual, carregarSessaoAtual

class Usuario:
    

    def __init__(self, nomeUsuario:str, senhaUsuario:str, bibliotecario=False):
        self.nomeUsuario = nomeUsuario
        self.senhaUsuario = senhaUsuario
        self.bibliotecario = bibliotecario
        self.livrosPossuidos = []


    def emprestarLivro(self, livro):
        livroDict = {"Titulo":livro["Titulo"], "Autor":livro["Autor"]}
        self.livrosPossuidos.append(livroDict)
        sessaoAtual(self.toDict())


    def toDict(self):
        userDict = {
            "User": self.nomeUsuario,
            "Password": self.senhaUsuario,
            "AdminAcess": self.bibliotecario,
            "LivrosPossuidos": self.livrosPossuidos
            }
        return userDict