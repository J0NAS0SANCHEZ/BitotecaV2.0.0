from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# Inicializa Firebase si no está ya inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")  # Reemplaza con tu ruta real
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/books", methods=["GET"])
def get_books():
    books_ref = db.collection("books")
    docs = books_ref.stream()
    books = [{**doc.to_dict(), "id": doc.id} for doc in docs]
    return jsonify(books)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
