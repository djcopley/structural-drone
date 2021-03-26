from skeyes.mvc.view.view import View
from skeyes.mvc.view.window import Window

from PyQt5.QtWidgets import QApplication


class GuiView(View):
    def __init__(self, controller):
        super().__init__(controller)
        self.app = QApplication([])

    def start(self):
        self.start_controller()
        window = Window()
        window.show()
        self.app.exec()

        # app.exec() blocks until window is closed by user
        self.stop()

    def stop(self):
        # Tell the controller to stop the model
        self.controller.stop()
