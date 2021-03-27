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
        self.actions = {
            "window": Actions.PAUSE,
            "gutter": Actions.PAUSE
        }

        # TODO Features should be loaded from names file

        self.drone = None

    def generate_action(self, feature):
        if self.actions[feature] == Actions.PAUSE:
            self.pause_mission()

    # TODO Yeah I don't know how I am going to implment the asyncio features with the rest of my codebase
    async def connect_to_drone(self, system_address="udp://:14540"):
        self.drone = System()
        await self.drone.connect(system_address=system_address)

    async def pause_mission(self):
        pass
