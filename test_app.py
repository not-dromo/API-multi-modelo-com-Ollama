import pytest 
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_models_sucesso(client):
    with patch('app.listar_modelos', return_value=['gemma3:1b', 'qwen2.5:1.5b']):
        resposta = client.get('/models')
        dados = resposta.get_json()

        assert resposta.status_code == 200
        assert dados == {"models": ['gemma3:1b', 'qwen2.5:1.5b']}

def test_models_ollama_indisponivel(client):
    with patch('app.listar_modelos', side_effect=Exception('erro de conexão')):
        resposta = client.get('/models')
        dados = resposta.get_json()

        assert resposta.status_code == 503
        assert 'erro' in dados


def test_generate_sucesso(client):
    class RespostaFalsa:
        class message:
            content = "resposta gerada pelo modelo"

    with patch('app.listar_modelos', return_value=['gemma3:1b']), \
         patch('app.chat', return_value=RespostaFalsa()):

        resposta = client.post('/generate', json={
            "model": "gemma3:1b",
            "prompt": "oi"
        })
        dados = resposta.get_json()

        assert resposta.status_code == 200
        assert dados == {"resposta": "resposta gerada pelo modelo"}


def test_generate_modelo_invalido(client):
    with patch('app.listar_modelos', return_value=['gemma3:1b']):
        resposta = client.post('/generate', json={
            "model": "modelo-que-nao-existe",
            "prompt": "oi"
        })
        dados = resposta.get_json()

        assert resposta.status_code == 400
        assert 'erro' in dados


def test_generate_erro_na_geracao(client):
    with patch('app.listar_modelos', return_value=['gemma3:1b']), \
         patch('app.chat', side_effect=Exception('falhou')):

        resposta = client.post('/generate', json={
            "model": "gemma3:1b",
            "prompt": "oi"
        })
        dados = resposta.get_json()

        assert resposta.status_code == 500
        assert 'erro' in dados