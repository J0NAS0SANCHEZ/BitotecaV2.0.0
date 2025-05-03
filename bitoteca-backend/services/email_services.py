import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
print(f"SENDGRID_API_KEY: {SENDGRID_API_KEY}")

def send_reminder_email(to_email, user_name, due_date):
    message = Mail(
        from_email='connorulloa2050@gmail.com',
        to_emails=to_email,
        subject='📚 Recordatorio de préstamo',
        html_content=f"""
        <strong>Hola {user_name},</strong><br>
        Este es un recordatorio de que tu libro debe devolverse antes del <strong>{due_date}</strong>.<br>
        ¡Gracias por usar Bitoteca!
        """)
    
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code == 202
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False
