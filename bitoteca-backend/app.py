from flask import Flask
from routes.email_routes import email_bp

app = Flask(__name__)
app.register_blueprint(email_bp)


# ... aqui va otros blueprints como /books, etc.

@app.route("/test-sendgrid")
def test_sendgrid_key():
    key = os.getenv("SENDGRID_API_KEY")
    return f"SendGrid key visible?: {key is not None}"


if __name__ == '__main__':
    app.run(debug=True)
