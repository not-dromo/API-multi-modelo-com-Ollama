async function enviarPergunta() {
    const pergunta = document.getElementById('pergunta').value;

    if (pergunta.trim() === ''){
        alert("Erro! Mensagem vazia.")
        return;
    }

    document.getElementById('pergunta').value = '';

    const resposta = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model: 'qwen3:4b', prompt: pergunta })
    });

    const dados = await resposta.json();
    console.log(dados.resposta);

    const chat = document.getElementById('chat');
    chat.innerHTML += `<div class="mensagem-sua"><b>Você:</b> ${pergunta}</div>`;
    chat.innerHTML += `<div class="mensagem-bot"><b>Modelo:</b> ${dados.resposta}</div>`;
}


document.getElementById('pergunta').addEventListener('keydown', function(evento) {
    if (evento.key === 'Enter' && !evento.shiftKey){
        evento.preventDefault();
        enviarPergunta();
    }
});