from flask import Flask, render_template, request, jsonify
from config import *
import traceback
import openai

app = Flask(__name__)

openai.api_key = OPENAI_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    
    data = request.get_json()

    prompt = ''
    if data['action'] == '1':
        prompt = f"Improve grammar in this text and give only the final text in output\n{data['text']}"
    elif data['action'] == '2':
        prompt = f"Make this email professional and give only the final text in output\n{data['text']}"
    elif data['action'] == '3':
        prompt = f"Change the text to {data['lang']} and give the final result in output\n{data['text']}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=2560,
        frequency_penalty=0,
        top_p=1
    )

    result = response.choices[0].message.content

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)