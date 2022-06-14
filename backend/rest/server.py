from flask import Flask

from rest.controller_interface import ControllerInterface


class Server:

    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run()

    def addController(self, controller: ControllerInterface):
        controller.set_endpoints(self.app)
