from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7270327815:AAFA21sujNji42HkWHAWfETYF9MFYwDOKEY"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["from"].get("first_name", "")
        text = data["message"].get("text", "")

        if text == "/start":
            reply = (
                f"👋 Hola {first_name}!\n\n"
                f"Este es tu chat ID de Telegram:\n\n"
                f"👉 {chat_id}\n\n"
                f"Cópialo y pégalo en el formulario web para recibir confirmación."
            )

            # Enviar el mensaje al usuario
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": reply
            }
            requests.post(url, json=payload)

    return "ok"
