from flask import Flask, session, request, render_template, redirect, url_for,  abort
from ollama import chat
from ollama import ChatResponse
#ollama pull [nome do modelo] --> para instalar um modelo
#ollama list --> pra ver os modelos instalados
#ollama rm [nome do modelo] --> para remover um modelo

# Setup
app = Flask(__name__)


# Rota para o menu
@app.route('/menu')
def index():
    
    return render_template('menu.html')

# Rota para processar conversa e gerar conversa
@app.route('/generate', methods=['POST'])
def generate():

    dados = request.get_json()
    pergunta = dados.get('prompt')

    # Teste: dados foram enviados?
    print(str(pergunta))
    print("\n\n")

    # Envia a mensagem para o modelo gemma3 e aguarda resposta
    # TODO: fazer o modelo não ser estático - permitir o usuário altera-lo
    resposta: ChatResponse = chat(model='gemma3:1b', messages=[
        {
            'role': 'user',
            'content': pergunta,
        },
    ])

    texto_resposta = resposta.message.content

    #print(texto_resposta)

    return {"resposta": texto_resposta}, 200

# Setup
if __name__ == '__main__':
    app.run(debug=True, port=5000)