from flask import redirect, url_for

from app.main.db import db, Todo


def delete_todo(todo_id: int):
    # todo: Todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo = Todo.query.filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo_router.render_all_todos"))

# def delete_todo(todo_id: int):
#     return f"Hello Delete Todo. id: {todo_id}"