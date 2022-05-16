from flask import Blueprint
from context.todo.main.controllers import (
    read_controller as read, 
    create_controller as create, 
    update_controller as update, 
    delete_controller as delete
)

todo_router = Blueprint("todo_router", __name__)

# Read
todo_router.route("/", methods=["GET"])(read.render_all_todos)
# Create
todo_router.route("/add", methods=["POST"])(create.create_todo)
# Update
todo_router.route("/update/<int:todo_id>", methods=["GET"])(update.update_todo)
# Delete
todo_router.route("/delete/<int:todo_id>", methods=["GET"])(delete.delete_todo)

