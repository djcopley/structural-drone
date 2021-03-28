#!/usr/bin/env python3

# Warning: Only try this in simulation!
#          The direct attitude interface is a low level interface to be used
#          with caution. On real vehicles the thrust values are likely not
#          adjusted properly and you need to close the loop using altitude.

import asyncio

from mavsdk import System
from mavsdk.offboard import (Attitude, OffboardError)


async def run():
    """ Does Offboard control using attitude commands. """

    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    v = input("Enter it: ")
    while v != "q":
        if v == "p":
            await drone.mission.pause_mission()
        elif v == "r":
            await drone.mission.start_mission()
        v = input("Enter it: ")

    # print("-- Arming")
    # await drone.action.arm()
    #
    # print("-- Setting initial setpoint")
    # await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.0))
    #
    # print("-- Starting offboard")
    # try:
    #     await drone.offboard.start()
    # except OffboardError as error:
    #     print(f"Starting offboard mode failed with error code: \
    #           {error._result.result}")
    #     print("-- Disarming")
    #     await drone.action.disarm()
    #     return
    #
    # print("-- Go up at 70% thrust")
    # await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.9))
    # await asyncio.sleep(2)
    #
    # print("-- Roll 30 at 60% thrust")
    # await drone.offboard.set_attitude(Attitude(30.0, 0.0, 0.0, 0.8))
    # await asyncio.sleep(2)
    #
    # print("-- Roll -30 at 60% thrust")
    # await drone.offboard.set_attitude(Attitude(-30.0, 0.0, 0.0, 0.8))
    # await asyncio.sleep(2)
    #
    # print("-- Hover at 60% thrust")
    # await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.8))
    # await asyncio.sleep(2)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: \
              {error._result.result}")

    await drone.action.land()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
