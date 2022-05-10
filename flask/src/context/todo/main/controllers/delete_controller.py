from flask import redirect, url_for

from app.main.db import db
from context.shared.db_models import Todo


def delete_todo(todo_id: int):
    todo: Todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))