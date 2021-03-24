from skeyes.mvc.model.action import Action


class Model:
    def __init__(self):
        self.running = True
        self.action = Action

    def start(self):
        while self.running:
            pass
