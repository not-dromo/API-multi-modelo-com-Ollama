from ollama import chat
from ollama import ChatResponse
#ollama pull [nome do modelo] --> para instalar um modelo
#ollama list --> pra ver os modelos instalados
#ollama rm [nome do modelo] --> para remover um modelo

response: ChatResponse = chat(model='gemma3:1b', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])

print(response['message']['content'])
print(response.message.content)