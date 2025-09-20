import requests
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('MTMwOTU0NTU2Nzg3MzAwNzY0Ng.GDjVVq.G9tKUPqvtQg6agbQVtba5wlOgknKvsuljNigss')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/acortar', methods=['POST'])
def acortar():
    url = request.form.get('url')
    ip = request.remote_addr
    
    # Acortar el enlace (simulación)
    enlace_acortado = f"https://acortado.com/{url[-8:]}"
    
    # Enviar notificación a Discord
    enviar_a_discord(url, enlace_acortado, ip)
    
    return jsonify({
        'original': url,
        'acortado': enlace_acortado
    })

def enviar_a_discord(url_original, url_acortada, ip):
    embed = {
        "title": "🔗 Nuevo Enlace Acortado",
        "color": 5814783,  # Color morado
        "fields": [
            {"name": "URL Original", "value": url_original, "inline": False},
            {"name": "URL Acortada", "value": url_acortada, "inline": False},
            {"name": "IP del Usuario", "value": ip, "inline": True}
        ]
    }
    
    data = {
        "embeds": [embed],
        "username": "Acortador de Enlaces",
        "avatar_url": "https://i.imgur.com/8Km9tLL.png"
    }
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        response.raise_for_status()
    except Exception as e:
        print(f"Error al enviar a Discord: {e}")

if __name__ == '__main__':
    app.run(debug=True)
