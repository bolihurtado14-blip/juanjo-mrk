# main.py
from flask import Flask, render_template, request, jsonify
from chatbot.data import training_data
from chatbot.model import build_and_train_model, load_model, predict_cluster
import random 

app = Flask(__name__)

# Intentamos cargar el modelo (o entrenamos si no existe)
model, vectorizer = load_model()
if model is None:
    model, vectorizer = build_and_train_model(training_data, n_clusters=6)  # ✅ Número de grupos ajustable



# Respuestas por grupo
Respuestas ={
    0:["¡Hola! ¿Cócomo estas?",
       "¡Qué gusto saludarte!",
       "¡Hola! ¿En que peudo ayudarte?",
       ],
    1:["Hasta luego",
       "Nosvemos pronto",
       "Cuidate Espero Verte de nuevo",
       ],
    2:["Soy un asistente virtual creado ppara ayudarte",
       "¡Por supuesto! ¿Con que necesitas ayuda",
       "Cuentame tu problema y buscare una solucion",
       ],
    3:["Puedo afrecerte infmormacion o resolver tus dudas",
       "¡En que te puedo ayudar",
       "Estoy aqui para resolrver tus respouestas",
       ],
    4:["¡Gracias a ti!",
       "De nada, me alregra ser de ayuda",
       "¡Muy amable de tu parte!",
       ],
    5:["Lamento que te sientas asi úedo internarlo de nuevo",
       "Parece que algo no salio bien, ¿Quieres que lo revisemos",
       " no siempre soy perfecto, pero puedo intentarll otra vez",
       ],
}
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.form.get("message", "")
    if not user_text.strip():
        return jsonify({"response": "Por favor escribe algo 😅"})

    # Predice el grupo al que pertenece el mensaje
    cluster = predict_cluster(model, vectorizer, user_text)

    # ✅ Mensaje más descriptivo
    #response = f"Tu mensaje pertenece al grupo {cluster}. Este grupo contiene frases con significados similares."
    response=random.choice(Respuestas.get(cluster,[
        "NO estoy seguro de enterder, pero puedo internarlo otra vez."
    ]))
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
