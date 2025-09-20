from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/acortar', methods=['POST'])
def acortar():
    url = request.form.get('url')
    # Aquí iría la lógica para acortar el enlace
    # Por ahora, simulamos una respuesta
    return jsonify({
        'original': url,
        'acortado': f"https://acortado.com/{url[-8:]}"
    })

if __name__ == '__main__':
    app.run(debug=True)
