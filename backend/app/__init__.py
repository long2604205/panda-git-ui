from flask import Flask
from app.config import init_app
from app.routes.routes import git_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    init_app(app)
    app.register_blueprint(git_bp)
    return app
