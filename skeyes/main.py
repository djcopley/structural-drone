import argparse

from skeyes.mvc.model.model import Model
from skeyes.mvc.view.cli_view import CliView
from skeyes.mvc.view.gui_view import GuiView
from skeyes.mvc.controller.controller import Controller


# from . import __version__
__version__ = "1.0"


def gui():
    main(GuiView)


def cli():
    main(CliView)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version",
                        action="version",
                        version=__version__)
    return parser.parse_args()


def main(view_backend):
    args = parse_args()
    model = Model()
    controller = Controller(model)
    view = view_backend(controller)
    view.start()


if __name__ == '__main__':
    main(CliView)
