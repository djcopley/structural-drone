import logging


class Controller:
    def __init__(self, model):
        self.model = model

    def start(self):
        self.model.start()

    def stop(self):
        self.model.running = False

    def set_qgc_ip(self, ip):
        pass

    def set_qgc_port(self, port):
        pass

    def set_logging_file_path(self, fp):
        pass

    def get_actions(self):
        return

    def set_action(self, img_class, action):
        pass
