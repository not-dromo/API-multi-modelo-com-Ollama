# API Multi-Modelo com Ollama

API REST em Flask que permite selecionar dinamicamente um modelo de linguagem disponível localmente via Ollama, enviar um prompt e receber a resposta gerada, com tempo de execução medido.

## Pré-requisitos

- Python 3.10+
- [Ollama](https://ollama.com) instalado e rodando localmente
- Pelo menos um modelo baixado no Ollama ➡ `ollama pull [nome do modelo desejado]`

## Instalação

```bash
git clone <https://github.com/not-dromo/API-multi-modelo-com-Ollama>
cd API_multi-modelo

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

## Configuração

Copie o arquivo de exemplo e ajuste se necessário:

```bash
cp .env.example .env
```

Variáveis disponíveis:

| Variável      | Descrição                          | Padrão                    |
|---------------|-------------------------------------|----------------------------|
| `OLLAMA_HOST` | Endereço do servidor Ollama         | `http://127.0.0.1:11434`  |
| `FLASK_PORT`  | Porta em que a API vai rodar        | `5000`                    |

## Execução

Com o Ollama rodando em segundo plano:

```bash
python app.py
```

A aplicação sobe em `http://localhost:5000` (ou na porta definida em `FLASK_PORT`).

- Interface web (chat): `http://localhost:5000/menu`
- Documentação interativa (Swagger): `http://localhost:5000/apidocs`

## Endpoints

| Método | Rota        | Descrição                                  |
|--------|-------------|---------------------------------------------|
| GET    | `/models`   | Lista os modelos disponíveis no Ollama       |
| POST   | `/generate` | Envia um prompt para um modelo e retorna a resposta |

Detalhes completos de parâmetros, formatos de resposta e códigos de erro estão documentados no Swagger (`/apidocs`).

## Testes automatizados

```bash
pytest test_app.py -v
```

## Experimento

Script que envia os mesmos prompts para múltiplos modelos e registra modelo, prompt, resposta e tempo de execução em um CSV.

Com o servidor rodando (`python app.py`) em outro terminal:

```bash
python experimento.py
```

Os resultados são salvos em `experimento.csv`.

## Estrutura do projeto

```
app.py                # rotas Flask
ollama_service.py     # comunicação com o Ollama
experimento.py         # script do experimento com múltiplos modelos
test_app.py            # testes automatizados
templates/menu.html    # interface do chat
static/script.js       # lógica do frontend
static/style.css       # estilos
.env.example           # exemplo de configuração
requirements.txt       # dependências do projeto
```

## Padrão de commits

Este projeto usa [gitmoji](https://gitmoji.dev) para categorizar commits:

- ✨ nova funcionalidade
- 🛡️ validação/segurança
- 🐛 correção de bug
- 📝 documentação
- ✅ testes
- ⚙️ configuração
- 💄 estilo/CSS
- 📦 dependências