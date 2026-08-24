from flask import Flask, session, request, render_template, redirect, url_for,  abort
from ollama import chat
from ollama import ChatResponse
#ollama pull [nome do modelo] --> para instalar um modelo
#ollama list --> pra ver os modelos instalados
#ollama rm [nome do modelo] --> para remover um modelo

# Setup
app = Flask(__name__)



# response: ChatResponse = chat(model='gemma3:1b', messages=[
#     {
#         'role': 'user',
#         'content': 'Why is the sky blue?',
#     },
# ])

# print(response['message']['content'])
# print(response.message.content)

# Rota para o menu
@app.route('/menu')
def index():
    
    return render_template('menu.html')

@app.route('/generate', methods=['POST'])
def generate():

    dados = request.get_json()
    pergunta = dados.get('prompt')

    # Teste: dados foram enviados?
    print(str(pergunta))
    print("\n\n")

    resposta: ChatResponse = chat(model='gemma3:1b', messages=[
        {
            'role': 'user',
            'content': pergunta,
        },
    ])

    print(resposta.message.content)

    return "ok"

# Setup
if __name__ == '__main__':
    app.run(debug=True, port=5000)