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