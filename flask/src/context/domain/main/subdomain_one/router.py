from flask import Blueprint
from context.domain.main.subdomain_one.controllers import read_controller

subdomain_one_router = Blueprint("subdomain_one_router", __name__)

# Read
subdomain_one_router.route("/subdomain_one", methods=["GET"])(read_controller.render_subdomain_one)
subdomain_one_router.route("/subdomain_one_extra", methods=["GET"])(read_controller.render_subdomain_one_extra)
# # Create
# todo_router.route("/add", methods=["POST"])(create.create_todo)
# # Update
# todo_router.route("/update/<int:todo_id>", methods=["GET"])(update.update_todo)
# # Delete
# todo_router.route("/delete/<int:todo_id>", methods=["GET"])(delete.delete_todo)