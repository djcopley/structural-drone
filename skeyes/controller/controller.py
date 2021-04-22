import logging

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self, model):
        """

        :param model:
        """
        self.model = model

    def start(self):
        """

        :return:
        """
        self.model.start()

    def stop(self):
        """

        :return:
        """
        self.model.stop()

    def set_qgc_ip(self, ip):
        """

        :param ip:
        :return:
        """
        self.model.set_qgc_ip(ip)

    def set_qgc_port(self, port):
        """

        :param port:
        :return:
        """
        self.model.set_qgc_port(port)

    def set_logging_file_path(self, fp):
        """

        :param fp:
        :return:
        """
        self.set_logging_file_path(fp)

    def get_actions(self):
        """

        :return:
        """
        return

    def set_action(self, img_class, action):
        """

        :param img_class:
        :param action:
        :return:
        """
        self.model.set_action(img_class, action)
