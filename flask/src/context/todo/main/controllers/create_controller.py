from flask import request, redirect, url_for

from app.main.db import db, Todo

def create_todo():
    title = request.form.get("title")
    new_todo = Todo(title = title, complete = False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo_router.render_all_todos"))

# def create_todo():
#     return "Hello Create Todo"