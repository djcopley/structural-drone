import argparse
import logging

from skeyes.model.model import Model
from skeyes.view.cli_view import CliView
from skeyes.view.gui_view import GuiView
from skeyes.controller.controller import Controller


# from . import __version__
__version__ = "1.0"
logger = logging.getLogger(__name__)


def gui():
    main(GuiView)


def cli():
    main(CliView)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version",
                        "-v",
                        action="version",
                        version=__version__)
    parser.add_argument("--debug",
                        "-d",
                        action="store_true",
                        default=False)
    return parser.parse_args()


def setup_logging():
    pass


def main(view_backend):
    args = parse_args()
    model = Model()
    controller = Controller(model)
    view = view_backend(controller)
    view.start()


if __name__ == '__main__':
    main(GuiView)
