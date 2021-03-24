import threading


class View:
    def __init__(self, controller):
        self.controller = controller
        self.t = threading.Thread(self.controller.run_model())
