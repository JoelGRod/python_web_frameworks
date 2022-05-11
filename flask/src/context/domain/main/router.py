from flask import Blueprint
from context.domain.main.subdomain_one.router import subdomain_one_router
from context.domain.main.subdomain_two.router import subdomain_two_router

domain_router = Blueprint("domain_router", __name__, url_prefix='/domain')

domain_router.register_blueprint(subdomain_one_router)
domain_router.register_blueprint(subdomain_two_router)
