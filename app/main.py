from flask import Flask
from app.controllers.books_controller import books_bp
from app.controllers.branches_controller import branches_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)
    # Register Blueprints
    app.register_blueprint(books_bp, url_prefix='/api')
    app.register_blueprint(branches_bp, url_prefix='/api')

    return app
