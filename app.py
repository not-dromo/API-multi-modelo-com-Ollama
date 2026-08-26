from flask import Flask, session, request, render_template, redirect, url_for,  abort
from ollama import chat
from ollama import ChatResponse
from ollama_service import listar_modelos
from flasgger import Swagger





app = Flask(__name__)
swagger = Swagger(app)





# Rota para o menu
@app.route('/menu')
def index():
    """
    Retorna a página HTML do chat
    ---
    tags:
      - Interface
    responses:
      200:
        description: Página HTML carregada com sucesso
    """
    
    return render_template('menu.html')

@app.route('/models', methods=['GET'])
def models():
    """
    Lista os modelos disponíveis no Ollama
    ---
    tags:
      - Modelos
    responses:
      200:
        description: Lista de modelos instalados
        examples:
          application/json: {"models": ["gemma3:1b", "qwen2.5:1.5b"]}
      503:
        description: Ollama indisponível
    """
    try:
        return {"models": listar_modelos()}, 200
    except Exception:
        return {"erro": "Ollama indisponível"}, 503

# Rota para processar conversa e gerar conversa
@app.route('/generate', methods=['POST'])
def generate():
    """
    Gera uma resposta usando o modelo escolhido
    ---
    tags:
      - Geração
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              example: gemma3:1b
            prompt:
              type: string
              example: Explique o que é uma variável
    responses:
      200:
        description: Resposta gerada com sucesso
      400:
        description: Modelo inválido ou prompt vazio
      500:
        description: Erro durante a geração
      503:
        description: Ollama indisponível
    """

    dados = request.get_json()
    pergunta = dados.get('prompt')
    modelo = dados.get('model')

    try:
        modelos_disponiveis = listar_modelos()
    except Exception:
        return {"erro": "Ollama indisponível"}, 503

    if modelo not in modelos_disponiveis:
        return {"erro": "esse modelo não existe"}, 400

    try:
        # Envia a mensagem para o modelo gemma3 e aguarda resposta
        resposta: ChatResponse = chat(model=modelo, messages=[
            {
                'role': 'user',
                'content': pergunta,
            },
        ])

    except Exception:
        return {"erro": "falha ao gerar resposta"}, 500

    texto_resposta = resposta.message.content

    return {"resposta": texto_resposta}, 200



# Setup
if __name__ == '__main__':
    app.run(debug=True, port=5000)





#ollama pull [nome do modelo]    -->    instala modelo
#ollama list                     -->    lista modelos instalados
#ollama rm   [nome do modelo]    -->    remove modelo