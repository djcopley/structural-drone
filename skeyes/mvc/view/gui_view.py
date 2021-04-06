from skeyes.mvc.view.view import View
from skeyes.mvc.view.window import Window

from PyQt5.QtWidgets import QApplication, QMessageBox


def valid_ipv4(ip):
    ip = ip.split(".")

    if len(ip) != 4:
        return False

    try:
        for group in ip:
            if not int(group) <= 255:
                raise ValueError
        return True

    except ValueError:
        return False


class GuiView(View):
    def __init__(self, controller):
        super().__init__(controller)
        self.app = QApplication([])
        self.window = Window()
        self.register_signals()

    def register_signals(self):
        self.window.windows_combo.activated[str].connect(self.update_windows_action)
        self.window.stream_enable_checkbox.toggled.connect(self.enable_video_stream)
        self.window.file_logging_enable_checkbox.toggled.connect(self.enable_file_logging)
        self.window.gst_ip.editingFinished.connect(self.set_qgc_ip)
        self.window.gst_port.editingFinished.connect(self.set_qgc_port)
        self.window.file_path_input.editingFinished.connect(self.set_logging_file_path)

    def start(self):
        self.start_controller()
        self.window.show()
        self.app.exec()

        # app.exec() blocks until window is closed by user
        self.stop()

    def stop(self):
        # Tell the controller to stop the model
        self.controller.stop()

    # TODO this should be dynamic based on available actions in the model. ALso not based on strings.
    def update_windows_action(self, action):
        self.controller.set_action("window", action.lower())

    def update_gutters_action(self, action):
        self.controller.set_action("gutter", action.lower())

    def enable_video_stream(self, enabled):
        self.window.qgc_label.setDisabled(not enabled)
        self.window.gst_ip.setDisabled(not enabled)
        self.window.streaming_port_label.setDisabled(not enabled)
        self.window.gst_port.setDisabled(not enabled)

    def set_qgc_ip(self):
        ip = self.window.gst_ip.text()

        if valid_ipv4(ip):  # Regex match that it is a valid ip address
            self.controller.set_qgc_ip(ip)
        else:
            self.window.gst_ip.setText("127.0.0.1")
            self.error_window("{} is not a valid IP address!".format(ip))

    def set_qgc_port(self):
        port = self.window.gst_port.text()
        try:
            if 0 < int(port) < 65535:
                self.controller.set_qgc_port(port)
        except ValueError:
            self.window.gst_port.setText("5600")
            self.error_window("{} is not a valid port!".format(port))

    def enable_file_logging(self, enabled):
        self.window.file_path_label.setDisabled(not enabled)
        self.window.file_path_input.setDisabled(not enabled)

    def set_logging_file_path(self):
        file_path = self.window.file_path_input.text()
        # TODO implement logging

    @staticmethod
    def error_window(text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()
