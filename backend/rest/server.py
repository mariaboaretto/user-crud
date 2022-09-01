from flask import Flask
from flask_cors import CORS

from rest.controller_interface import ControllerInterface


class Server:

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, methods=["GET", "POST", "DELETE", "PUT"])

    def run(self):
        self.app.run()

    def addController(self, controller: ControllerInterface):
        controller.set_endpoints(self.app)
