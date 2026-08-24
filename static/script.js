async function enviarPergunta() {
    const pergunta = document.getElementById('pergunta').value;
    document.getElementById('pergunta').value = '';

    const resposta = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model: 'qwen3:4b', prompt: pergunta })
    });

    const dados = await resposta.json();
    console.log(dados.resposta);

    const chat = document.getElementById('chat');
    chat.innerHTML += `<p><b>Você:</b> ${pergunta}</p>`;
    chat.innerHTML += `<p><b>Modelo:</b> ${dados.resposta}</p>`;
}


document.getElementById('pergunta').addEventListener('keydown', function(evento) {
    if (evento.key === 'Enter' && !evento.shiftKey){
        evento.preventDefault();
        enviarPergunta();
    }
});