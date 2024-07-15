from flask import Flask
from app.controllers.books_controller import books_bp
from app.controllers.branches_controller import branches_bp
from app.controllers.copies_controller import copies_bp
from app.controllers.transactions_controller import transactions_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)
    # Register Blueprints
    app.register_blueprint(books_bp, url_prefix='/api')
    app.register_blueprint(branches_bp, url_prefix='/api')
    app.register_blueprint(copies_bp, url_prefix='/api')

    app.register_blueprint(transactions_bp, url_prefix='/api')

    return app
