import logging
import asyncio

from enum import Enum
from mavsdk import System
from mavsdk.mission import MissionPlan, MissionItem

logger = logging.getLogger(__name__)


class Actions(Enum):
    IGNORE = "ignore"
    PAUSE = "pause"


class Action:
    def __init__(self):
        """

        """
        self.actions = {
            "window": Actions.PAUSE,
            "gutter": Actions.PAUSE
        }

        self.drone = None

    def generate_action(self, feature):
        """

        :param feature:
        :return:
        """
        if self.actions[feature] == Actions.PAUSE:
            self.pause_mission()

    # TODO Yeah I don't know how I am going to implment the asyncio features with the rest of my codebase
    async def connect_to_drone(self, system_address="udp://:14540"):
        """

        :param system_address:
        :return:
        """
        self.drone = System()
        await self.drone.connect(system_address=system_address)

    async def pause_mission(self):
        """

        :return:
        """
        await self.drone.mission.pause_mission()

    def set_action(self, img_class, action):
        """

        :param img_class:
        :param action:
        :return:
        """
        logger.debug("Action updated: class={}, action={}".format(img_class, action))
        self.actions[img_class] = action
