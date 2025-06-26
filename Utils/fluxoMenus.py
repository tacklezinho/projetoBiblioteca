from Classes.Livro import Livro
from Classes.Biblioteca import Biblioteca
from Utils.tools import livroExiste
from Classes.Usuario import Usuario
from Classes.Autenticador import Autenticador



def fluxoAdicionarLivro(biblioteca : Biblioteca) -> None:
    tituloLivro = str(input("Digite o titulo do livro: "))
    autorLivro = str(input("Digite o autor do livro: "))
    livro = Livro(titulo=tituloLivro, autor=autorLivro)
    if livroExiste(titulo=tituloLivro, biblioteca=biblioteca):
        print("\n--- Esse livro que está tentando adicionar já existe ---\n")
    else:
        biblioteca.adicionarLivro(livro=livro)

def fluxoRetirarLivro(biblioteca : Biblioteca) -> None:
    tituloLivro = str(input("Digite o titulo que deseja retirar: "))
    if livroExiste(titulo=tituloLivro, biblioteca=biblioteca):
        if biblioteca.verificarDisponibilidade(tituloLivro=tituloLivro):
            biblioteca.removerLivro(titulo=tituloLivro)
            print("\n-- Livro removido com sucesso! --")
        else:
            print("\n-- Livro não está disponível --")
    else:
        print("\n--- Livro não encontrado! ---\n")

def fluxoListarLivros(biblioteca : Biblioteca) -> None:
    # Mostrar Somente os Livros Disponiveis
    biblioteca.listarLivros()

def fluxoBuscarLivro(biblioteca: Biblioteca):
    tituloLivro = str(input("Digite o titulo que deseja buscar: "))
    if livroExiste(titulo=tituloLivro, biblioteca=biblioteca):
        livroDict = biblioteca.buscarLivro(titulo=tituloLivro)
        print(f"""\nTitulo: {livroDict["Titulo"]}\nAutor: {livroDict["Autor"]}\nDisponivel: {livroDict["Disponivel"]}""")
    else:
        print("\n-- Livro não encontrado --")

def fluxoEmprestarLivro(usuarioAtual:Usuario, biblioteca:Biblioteca, autenticador: Autenticador):
        tituloLivro = str(input("Digite o titulo que deseja retirar: "))
        livro = biblioteca.buscarLivro(titulo=tituloLivro)
        if livro == None:
            print("\nLivro não encontrado!")
        else:
            if biblioteca.verificarDisponibilidade(livro["Titulo"]):
                usuarioAtual.emprestarLivro(livro=livro)
                biblioteca.alterarDisponibilidade(livro["Titulo"])
                autenticador.atualizarUsuarios(usuarioAtual.toDict())
                print("\n-- Livro Emprestado Com Sucesso --")
            else:
                print("\n-- Livro Não Está Disponivel --")

def fluxoDevolverLivro(biblioteca: Biblioteca, userAtual: Usuario, autenticador:Autenticador):
    userAtual.listarLivrosPessoais() #Print Seus Livros
    tituloLivro = str(input("\nDigite o título que deseja devolver: ")) # Qual Livro Deseja Devolver
    if userAtual.devolverLivro(tituloLivro=tituloLivro):
        biblioteca.alterarDisponibilidade(tituloLivro=tituloLivro)
        autenticador.atualizarUsuarios(userAtual.toDict())
        print("\n-- Livro devolvido com sucesso --")
    else:
        print("\n-- Erro ao devolver o livro --")
    
    userAtual# Remover Livro da Sessao e do Db
    # Alterar Disponibilidade

def fluxoTornarBibliotecario(autenticador:Autenticador):
    nomeUser = str(input("Digite o nome de usuário que deseja tornar bibliotecário: "))
    if not autenticador.verificarAdminAcess(username=nomeUser):
        if autenticador.tornarBibliotecario(username=nomeUser):
            print("\n-- Usuário alterado com sucesso! --")
    else:
        print("\n-- Usuário já é bibliotecário --")