import logging


class Controller:
    def __init__(self, model):
        self.model = model

    def start(self):
        self.model.start()

    def stop(self):
        self.model.stop()

    def set_qgc_ip(self, ip):
        self.model.set_qgc_ip(ip)

    def set_qgc_port(self, port):
        self.model.set_qgc_port(port)

    def set_logging_file_path(self, fp):
        self.set_logging_file_path(fp)

    def get_actions(self):
        return

    def set_action(self, img_class, action):
        self.model.set_action(img_class, action)
