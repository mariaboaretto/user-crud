from flask import Flask, jsonify, request
from core.user_service_factory import UserServiceFactory
from rest.controller_interface import ControllerInterface


class UserController(ControllerInterface):

    def __init__(self):
        self.user_service = UserServiceFactory.get()

    def set_endpoints(self, app: Flask) -> None:
        # Get all users
        @app.get("/users/")
        def get_users():
            users = []
            search_txt = request.args.get("search_txt")

            # If search text is none or an empty string, return all users
            if search_txt is None or search_txt == "":
                for user in self.user_service.get_all_users():
                    user_dict = {"user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name,
                                 "email": user.email, "username": user.username}
                    users.append(user_dict)
            # Otherwise, filter users by search text
            else:
                for user in self.user_service.filter_users(search_txt):
                    user_dict = {"user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name,
                                 "email": user.email, "username": user.username}
                    users.append(user_dict)

            return jsonify(users)

        @app.get("/users/<int:user_id>/")
        def get_user_by_user_id(user_id):
            try:
                user = self.user_service.find_user_by_user_id(user_id)
                return {"user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name,
                        "email": user.email, "username": user.username}
            except Exception as e:
                return {"message": "{}".format(e)}, 404

        @app.post("/users/")
        def create_user():
            if request.is_json:
                try:
                    user = request.get_json()
                    self.user_service.create_user(user["first_name"], user["last_name"], user["email"],
                                                  user["username"],
                                                  user["password"])
                    new_user = self.user_service.filter_users(user["username"])[0]
                    return {"user_id": new_user.user_id, "first_name": new_user.first_name,
                            "last_name": new_user.last_name,
                            "email": new_user.email, "username": new_user.username}, 201
                except Exception as e:
                    return {"message": "{}".format(e)}, 400

        @app.delete("/users/<int:user_id>/")
        def delete_user(user_id):
            try:
                self.user_service.remove_user_by_id(user_id)
            except Exception as e:
                return {"message": "{}".format(e)}, 404

            return {"message": "User Removed Successfully"}, 200

        # Updates user's first and last names
        @app.put("/users/<int:user_id>/")
        def update_user(user_id):
            if request.is_json:
                try:
                    new_info = request.get_json()
                    self.user_service.update_user_info(user_id, new_info["first_name"], new_info["last_name"])
                    user = self.user_service.find_user_by_user_id(user_id)

                    return {"user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name,
                            "email": user.email, "username": user.username}
                except Exception as e:
                    return {"message": "{}".format(e)}, 400

            return {"message": "Request must be JSON"}, 400

        @app.put("/users/password/<int:user_id>/")
        def update_password(user_id):
            if request.is_json:
                try:
                    info = request.get_json()
                    self.user_service.update_user_password(user_id, info["current_password"], info["new_password"],
                                                           info["password_confirmation"])
                    return {"message": "Password updated successfully!"}, 200
                except Exception as e:
                    return {"message": "{}".format(e)}, 400

            return {"message": "Request must be JSON"}, 400
