import os 
from flask import Flask, jsonify
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore


#Cargamos las variables de entorno 
load_dotenv()

#iniciamos firebase Admin


cred_path = "firebase.json"
print("¿Existe el archivo?:", os.path.exists(cred_path))

#cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
  return "¡API conectada a Firebase!"

@app.route('/test-firestore')
def test_firestore():
  # Ejemplo: leer libros
  books_ref = db.collection('books')
  docs = books_ref.stream()
  books = [{doc.id: doc.to_dict()} for doc in docs]
  return jsonify(books)

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 8080))
  app.run(host='0.0.0.0', port=port)