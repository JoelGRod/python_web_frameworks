from flask import render_template

from app.main.db import db, Todo


def render_all_todos():
    todo_list = db.session.query(Todo).all()
    # todo_list = Todo.query.all()
    return render_template("base.html", todo_list = todo_list)

# def render_all_todos():
#     return "Hello Read Todo"