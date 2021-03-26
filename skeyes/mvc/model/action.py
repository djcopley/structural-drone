from enum import Enum


class Actions(Enum):
    IGNORE = "ignore"
    PAUSE = "pause"


class Action:
    def __init__(self):
        self.actions = {
            "window": Actions.PAUSE,
            "gutter": Actions.PAUSE
        }

    def generate_action(self):
        pass
