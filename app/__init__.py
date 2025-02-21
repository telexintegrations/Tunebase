#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()
def create_app():
    app = Flask(__name__)

    CORS(app)

    from app.routes import routes

    app.register_blueprint(routes)