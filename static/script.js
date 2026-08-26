let processando = false;

async function carregarModelos() {
    const resposta = await fetch('/models');
    const dados = await resposta.json();

    const select = document.getElementById('modelo');
    select.innerHTML = ''; //limpa o "carregando modelos..." do html

    dados.models.forEach(nomeModelo => {
        const opcao = document.createElement('option');
        opcao.value = nomeModelo;
        opcao.textContent = nomeModelo;
        select.appendChild(opcao);        
    });
}

async function enviarPergunta() {
    const pergunta = document.getElementById('pergunta').value;

    //checa se a mensagem é vazia
    if (pergunta.trim() === ''){
        alert("Erro! Mensagem vazia.")
        return;
    }

    //checa se já tem uma mensagem sendo processada
    if (processando) return;
    processando = true;

    //limpa e bloqueia a caixa de texto
    document.getElementById('pergunta').disabled = true;
    document.getElementById('pergunta').value = '';

    //gera resposta
    const modeloEscolhido = document.getElementById('modelo').value;
    try {
        const resposta = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ model: modeloEscolhido, prompt: pergunta })
        });

        const dados = await resposta.json();
        console.log(dados.resposta);

        const chat = document.getElementById('chat');
        chat.innerHTML += `<div class="mensagem-sua"><b>Você:</b> ${pergunta}</div>`;
        chat.innerHTML += `<div class="mensagem-bot"><b>Modelo ${modeloEscolhido}:</b> ${dados.resposta}</div>`;
        chat.scrollTop = chat.scrollHeight;
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

//chamada de funções
window.addEventListener('DOMContentLoaded', carregarModelos);