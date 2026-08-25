let processando = false;

async function enviarPergunta() {

    //checa se já tem uma mensagem sendo processada
    if (processando) return;
    processando = true;

    const pergunta = document.getElementById('pergunta').value;

    //checa se a mensagem é vazia
    if (pergunta.trim() === ''){
        alert("Erro! Mensagem vazia.")
        return;
    }

    //limpa e bloqueia a caixa de texto
    document.getElementById('pergunta').disabled = true;
    document.getElementById('pergunta').value = '';

    //gera resposta
    try {
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
    } finally {
        processando = false;
        document.getElementById('pergunta').disabled = false;
    }
}


document.getElementById('pergunta').addEventListener('keydown', function(evento) {
    if (evento.key === 'Enter' && !evento.shiftKey){
        evento.preventDefault();
        enviarPergunta();
    }
});