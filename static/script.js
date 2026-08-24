async function enviarPergunta() {
    const pergunta = document.getElementById('pergunta').value;

    const resposta = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model: 'qwen3:4b', prompt: pergunta })
    });

    const dados = await resposta.json();
    console.log(dados.response);

}