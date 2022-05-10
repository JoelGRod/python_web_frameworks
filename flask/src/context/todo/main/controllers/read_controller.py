from flask import render_template

from app.main.db import db
from context.shared.db_models import Todo


# def render_all_todos():
#     todo_list = db.session.query(Todo).all()
#     return render_template("base.html", todo_list = todo_list)

def render_all_todos():
    return "Hello Read Todo"