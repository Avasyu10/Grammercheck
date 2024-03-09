function submitRequest() {
    const textfile = document.getElementById('textfile').value;
    const text = document.getElementById('text').value;
    const action = document.getElementById('action').value;
    const langInput = document.getElementById('langInput');
    const lang = document.getElementById('lang').value;

    if (action === '3') {
        langInput.style.display = 'block';
    } else {
        langInput.style.display = 'none';
    }
    console.log(JSON.stringify({
        textfile,
        text,
        action,
        lang,
    }));

    fetch('/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            textfile,
            text,
            action,
            lang,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('result').innerText = 'The result is: ${data.result}';
    })
    .catch(error => console.error('Error:', error));
}
