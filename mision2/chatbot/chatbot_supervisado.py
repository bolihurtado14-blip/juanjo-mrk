from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def build_and_train_model(train_pairs):
    questions = [q for q, _ in train_pairs]
    answers = [a for _, a in train_pairs]
    vectorizer = CountVectorizer()
    x=vectorizer.fit_transform(questions)

    unique_answers = sorted(set(answers))
    answers_to_label= {a:i for i,a in enumerate(unique_answers)}
    y = [answers_to_label[a] for a in answers]
    model = MultinomialNB()
    model.fit (x,y)
    return model, vectorizer, unique_answers
def predict_answer(model, vectorizer, unique_answers, user_text):
        x = vectorizer.transform([user_text])
        label = model.predict(x)[0]
        return unique_answers[label]
if __name__ == "__main__":
    training_data =[
        ("hola","Hola ¿En que te puedo ayudar?"),
        ("buenos dias","Buenos dias"),
        ("como estas","Estoy bien gracias por preguntar"),
        ("tu nombre","Soy un chatbot de ejemplo"),
        ("que puedes hacer","Puedo responder preguntas simples base"),
    ]
model, vectorizer, unique_answers= build_and_train_model(training_data)
print("Chatbor supervisado listo, Escribe 'salir' para trerminar")

while True:
    user = input("Tu: ").strip()
    if user.lower() in {"salir","exit","quit"}:
        print("bot: Hasta Pronto")
        break
    response = predict_answer(model, vectorizer, unique_answers,user)
    print("Bot", response)