from flask import Blueprint
from .services import (delete_User_data_by_id_service, get_all_users_service,
                       get_user_by_id_service, update_user_by_id_service, login, logout, register)

users = Blueprint("users", __name__)


@users.route("/user/login", methods=['Post'])
def login_user():
    return login()


@users.route("/user/logout", methods=['GET'])
def logout_user():
    return logout()


@users.route("/user/register", methods=["POST"])
def add_user():
    return register()


@users.route("/user/all", methods=["GET"])
def get_all_users():
    return get_all_users_service()


@users.route("/user/<int:id>", methods=["GET"])
def get_user_by_email(id):
    return get_user_by_id_service(id)


@users.route("/user/<int:id>", methods=["PUT"])
def update_user_by_id(id):
    return update_user_by_id_service(id)


@users.route("/user/<int:id>", methods=["DELETE"])
def delete_user_by_id(id):
    return delete_User_data_by_id_service(id)
