import argparse

from skeyes.mvc.model.model import Model
from skeyes.mvc.view.view import View
from skeyes.mvc.view.cli_view import CliView
from skeyes.mvc.view.gui_view import GuiView
from skeyes.mvc.controller.controller import Controller
from PyQt5.QtWidgets import QApplication, QLabel


# from . import __version__
__version__ = "1.0"


def gui():
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec()


def cli():
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version",
                        action="version",
                        version=__version__)
    return parser.parse_args()


def main():
    args = parse_args()
    model = Model()
    controller = Controller(model)
    view = View(controller)


if __name__ == '__main__':
    main()
