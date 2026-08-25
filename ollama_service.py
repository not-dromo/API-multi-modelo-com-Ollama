import ollama

def listar_modelos():
    resposta = ollama.list()
    return [modelo.model for modelo in resposta.models]