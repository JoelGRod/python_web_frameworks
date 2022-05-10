from crypt import methods
from flask import Blueprint
from context.todo.main.controllers import read, create, update, delete


# create = Blueprint("create", __name__)
# read = Blueprint("read", __name__)
# update = Blueprint("update", __name__)
# delete = Blueprint("delete", __name__)

todos_bp = Blueprint("todos_bp", __name__)

todos_bp.route("/", methods=["GET"])(read.render_all_todos)
todos_bp.route("/add", methods=["POST"])(create.create_todo)
todos_bp.route("/update/<int:todo_id>", methods=["GET"])(update.update_todo)
todos_bp.route("/delete/<int:todo_id>", methods=["GET"])(delete.delete_todo)

# read.route("/home", methods=["GET"])(read.render_all_todos)
# create.route("/add", methods=["POST"])(create.create_todo)
# update.route("/update/<int:todo_id>", methods=["GET"])(update.update_todo)
# delete.route("/delete/<int:todo_id>", methods=["GET"])(delete.delete_todo)