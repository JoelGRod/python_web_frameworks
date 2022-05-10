from flask import redirect, url_for

from app.main.db import db
from context.shared.db_models import Todo


# def update_todo(todo_id: int):
#     todo: Todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
#     todo.complete = not todo.complete
#     db.session.commit()
#     return redirect(url_for("home"))

def update_todo(todo_id: int):
    return f"Hello Update Todo. id: {todo_id}"