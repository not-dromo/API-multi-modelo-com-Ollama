from flask import Flask, session, request, render_template, redirect, url_for,  abort
from ollama import chat
from ollama import ChatResponse
from ollama_service import listar_modelos





app = Flask(__name__)





# Rota para o menu
@app.route('/menu')
def index():
    
    return render_template('menu.html')

@app.route('/models', methods=['GET'])
def models():
    try:
        return {"models": listar_modelos()}, 200
    except Exception:
        return {"erro": "Ollama indisponível"}, 503

# Rota para processar conversa e gerar conversa
@app.route('/generate', methods=['POST'])
def generate():

    dados = request.get_json()
    pergunta = dados.get('prompt')
    modelo = dados.get('model')

    try:
        if modelo not in listar_modelos():
            return {"erro": "esse modelo não existe"}, 400

        # Envia a mensagem para o modelo gemma3 e aguarda resposta
        resposta: ChatResponse = chat(model=modelo, messages=[
            {
                'role': 'user',
                'content': pergunta,
            },
        ])

        texto_resposta = resposta.message.content

        return {"resposta": texto_resposta}, 200
    except Exception:
        return {"erro": "Ollama indisponível"}, 503




# Setup
if __name__ == '__main__':
    app.run(debug=True, port=5000)





#ollama pull [nome do modelo]    -->    instala modelo
#ollama list                     -->    lista modelos instalados
#ollama rm   [nome do modelo]    -->    remove modelo