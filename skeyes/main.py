import argparse

from . import __version__


def gui():
    pass


def cli():
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version",
                        action="version",
                        version=__version__)
    return parser.parse_args()


def main():
    pass


if __name__ == '__main__':
    main()
