from flask import Flask
from routes.email_routes import email_bp

app = flask(__name__)
app.register_blueprint(email_bp)


# ... aqui va otros blueprints como /books, etc.

if __name__ == '__main__':
    app.run(debug=True)