from flask import Flask
from app.main.config import config
from app.main.db import db

from context.router import todo_router, domain_router

def create_app():
    app = Flask(__name__)

    app.config.from_object(config.DevConfig)

    db.init_app(app)

    app.register_blueprint(todo_router)
    app.register_blueprint(domain_router)

    return app



