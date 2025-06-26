from Classes.Autenticador import Autenticador
from Classes.Usuario import Usuario
from Utils.jsonHandler import carregarSessaoAtual, sessaoAtual

def fluxoLoginUsuario(autenticador:Autenticador) -> bool:
    userInput = str(input("\n\nDigite o nome de usuario: "))
    passInput = str(input("Digite a senha do usuario: "))
    if autenticador.loginUser(userLogin=userInput, passLogin=passInput): #Verifica se existe um usuario e senha no banco de dados -> True or False
        sessaoAtual(usuario=autenticador.usuarioNoBancoDeDados(username=userInput))
        print("\nUsuario Logado Com Sucesso!")
        return True
    else:
        print("\nUsuario ou Senha Invalidos!")



def fluxoCadastroUsuario(autenticador:Autenticador) -> None:
    userInput = str(input("\n\nDigite o nome de usuario: "))
    passInput = str(input("Digite a senha do usuario: "))
    usuario = Usuario(nomeUsuario=userInput, senhaUsuario=passInput)
    if autenticador.cadastroUser(usuario): #Cria o usuario no banco de dados
        print("\n-- Usuario Cadastrado Com Sucesso! --")

def getSessaoAtual() -> Usuario:
    dados = carregarSessaoAtual()
    user = Usuario(nomeUsuario=dados["User"], senhaUsuario=dados["Password"], bibliotecario=dados["AdminAcess"])
    return user