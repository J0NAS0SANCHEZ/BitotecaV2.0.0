from flask import Blueprint, request, jsonify
from services.email_services import send_reminder_email

email_bp = Blueprint('email_bp', __name__)

@email.bp.route("/send-reminder", methods=["post"])
def send_reminder():
  data = request.get_json()
  to_email = data.get("email")
  user_name = data.get("name")
  due_date = data.get("due_date")

if not all ([to_email, user_name, due_date]):
  return jsonify({"error": "Faltan datos"}), 400

if send_remider_email(to_email, user_name, due_date):
  return jsonfy({"messaje": "Correo enviado exitosamente"}), 200 

else:
  return jsonify({"error": "Error al enviar el correo"}), 500 
