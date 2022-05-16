from flask import Blueprint
from context.domain.main.subdomain_two.controllers import read_controller as read

subdomain_two_router = Blueprint("subdomain_two_router", __name__)

# Read
subdomain_two_router.route("/subdomain_two", methods=["GET"])(read.render_subdomain_two)
# # Create
# todo_router.route("/add", methods=["POST"])(create.create_todo)
# # Update
# todo_router.route("/update/<int:todo_id>", methods=["GET"])(update.update_todo)
# # Delete
# todo_router.route("/delete/<int:todo_id>", methods=["GET"])(delete.delete_todo)