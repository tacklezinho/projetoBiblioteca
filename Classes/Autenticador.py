from Utils.jsonHandler import carregarDadosDatabaseUser, salvarDadosDatabaseUser, criadorJsonDatabaseUser, sessaoAtual
from Classes.Usuario import Usuario

class Autenticador:

    def __init__(self):
        criadorJsonDatabaseUser()
        self.usuariosDatabase = carregarDadosDatabaseUser()

    def cadastroUser(self, usuario:Usuario):
        if isinstance(usuario, Usuario):
            if not self.usuarioExiste(username=usuario.nomeUsuario):
                userDict = {"User":usuario.nomeUsuario, "Password":usuario.senhaUsuario, "AdminAcess":usuario.bibliotecario, "LivrosPossuidos":usuario.livrosPossuidos}
                self.usuariosDatabase["Usuarios"].append(userDict)
                salvarDadosDatabaseUser(usuariosDatabase=self.usuariosDatabase)
                return True
            else:
                print("\n-- Usuário já existe --")
                return False
        else:
            print("\nAdicione apenas objetos do tipo Usuario")
            return False

    def loginUser(self, userLogin:str, passLogin:str) -> bool:
        dadosUsuarios = self.usuariosDatabase["Usuarios"]
        for usuario in dadosUsuarios:
            if usuario["User"] == userLogin and usuario["Password"] == passLogin:
                return True
        return False

    def usuarioNoBancoDeDados(self, username:str) -> dict:
        dadosUsuarios = self.usuariosDatabase["Usuarios"]
        for usuario in dadosUsuarios:
            if usuario["User"] == username:
                return usuario
            

    def usuarioExiste(self, username:str):
        if self.usuarioNoBancoDeDados(username=username) != None:
            return True
        else:
            return False        

    def atualizarUsuarios(self, userAtual:dict):
        if self.usuarioExiste(username=userAtual["User"]):
            self.removerUser(username=userAtual["User"])
            self.usuariosDatabase["Usuarios"].append(userAtual)
            salvarDadosDatabaseUser(self.usuariosDatabase)


    def removerUser(self, username:str):
        usuarios = self.usuariosDatabase["Usuarios"]
        for contagem, user in enumerate(usuarios):
            if user["User"] == username:
                del usuarios[contagem]
                salvarDadosDatabaseUser(usuariosDatabase=self.usuariosDatabase)

    
    def tornarBibliotecario(self, username:str):
        if self.usuarioExiste(username=username):
            userDict = self.usuarioNoBancoDeDados(username=username)
            userDict["AdminAcess"]=True
            self.atualizarUsuarios(userDict)
            return True
        else:
            print("-- Usuario não existe --")


    def verificarAdminAcess(self, username:str):
        userDict = self.usuarioNoBancoDeDados(username=username)
        if userDict["AdminAcess"] == True:
            return True
        else:
            return False
