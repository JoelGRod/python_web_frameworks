from flask import Flask
from app.main.config import config
from app.main.db import db

from context.routes import todos_bp

app = Flask(__name__)

app.config.from_object(config.DevConfig)

db.init_app(app)

app.register_blueprint(todos_bp, url_prefix='/')



