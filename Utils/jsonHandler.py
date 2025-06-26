import json
import os


def criadorJsonDatabase():
      caminho = os.path.join("Database", "livros.json")
      os.makedirs("Database", exist_ok=True)

      if not os.path.exists(caminho):
            with open(caminho, "w") as file:
                  json.dump({"Livros": []}, file, indent=2)


def carregarDadosDatabase():
        with open(r"Database/livros.json", "r") as file:
            return json.load(file)
        
def salvarDadosDatabase(livrosDatabase):
      with open(r"Database/livros.json", "w") as file:
            json.dump(livrosDatabase, file, indent=2)






def criadorJsonDatabaseUser():
      caminho = os.path.join("Database", "usuarios.json")
      os.makedirs("Database", exist_ok=True)

      if not os.path.exists(caminho):
            with open(caminho, "w") as file:
                  json.dump({"Usuarios": []}, file, indent=2)


def carregarDadosDatabaseUser():
        with open(r"Database/usuarios.json", "r") as file:
            return json.load(file)

def salvarDadosDatabaseUser(usuariosDatabase):
      with open(r"Database/usuarios.json", "w") as file:
            json.dump(usuariosDatabase, file, indent=2)



def sessaoAtual(usuario:dict):
      caminho = os.path.join("Database", "sessaoAtual.json")
      os.makedirs("Database", exist_ok=True)

      if not os.path.exists(caminho):
            with open(caminho, "w") as file:
                  json.dump({"Sessao": []}, file, indent=2)


      with open(r"Database/sessaoAtual.json", "w") as file:
            json.dump(usuario, file, indent=2)


def carregarSessaoAtual() -> dict:
      with open(r"Database/sessaoAtual.json", "r") as file:
            return json.load(file)