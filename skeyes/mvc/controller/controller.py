import logging


class Controller:
    def __init__(self, model):
        self.model = model

    def start(self):
        self.model.start()

    def stop(self):
        self.model.running = False

    def get_actions(self):
        return

    def set_action(self, img_class, action):
        pass
