from dotenv import load_dotenv
import requests
import csv
import os

load_dotenv()

FLASK_PORT = int(os.getenv('FLASKPORT', 5000))
URL_BASE = f'http://localhost:{FLASK_PORT}/generate'

MODELOS = [
    'gemma3:1b',
    'qwen2.5:1.5b'
]

PROMPTS = [
    "Qual a diferença de uma linguagem compilada e uma linguagem interpretada?",
    "Se houvesse uma luta entre habitantes do Uruguai e os cangurus da Austrália, quantos Cangurus cada Uruguaiano iria enfrentear?",
    "Como você resolveria o seguinte problema de matemática: a^n + b^n = c^n onde n > 2 e a,b,c são números reais positivos diferentes de zero"
]

resultados = []

i = 0

for modelo in MODELOS:
    for prompt in PROMPTS:
        resposta = requests.post(URL_BASE, json = {
            "model": modelo,
            "prompt": prompt
        })
        dados = resposta.json()

        i += 1
        print(f"pergunta {i} respondida!")

        resultados.append({
            "model": dados.get("model"),
            "prompt": prompt,
            "response": dados.get("response"),
            "time": dados.get("time")
        })

with open('experimento.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["model", "prompt", "response", "time"])
    escritor.writeheader()
    escritor.writerows(resultados)

print("Experimento concluído, resultados salvos em experimento.csv")