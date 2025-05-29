from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Tu token de bot de Telegram
TOKEN = "7270327815:AAFA21sujNji42HkWHAWfETYF9MFYwDOKEY"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["from"].get("first_name", "")
        text = data["message"].get("text", "")

        if text == "/start":
            mensaje = (
                f"👋 ¡Hola {first_name}!\n\n"
                f"Este es tu chat ID de Telegram:\n\n"
                f"👉 {chat_id}\n\n"
                f"Cópialo y pégalo en el formulario web para recibir confirmación automática."
            )

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": mensaje
            }
            requests.post(url, json=payload)

    return "ok"

if __name__ == '__main__':
    # Importante: Render usa una variable de entorno llamada PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

