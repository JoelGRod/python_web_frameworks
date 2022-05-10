from flask import request, redirect, url_for

from app.main.db import db
from context.shared.db_models import Todo

def create_todo():
    title = request.form.get("title")
    new_todo = Todo(title = title, complete = False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))