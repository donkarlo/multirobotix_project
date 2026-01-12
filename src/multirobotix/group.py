from abc import ABC
from typing import List
from robotix.robot import Robot
from robotix.structure.kind.mind.goal.composite.goal import Goal


class Group(ABC):
    """
    A set of robots whose states are intra related through commands
    """
    def __init__(self, members:List[Robot], homogeneity):
        self._homogeneity = homogeneity
        self._members = members

    def add_robot(self, robot:Robot)->None:
        # TODO: check for uniquness
        self._members.append(robot)

    def get_members(self)->List[Robot]:
        return self._members

    def achieve_mission(self, robot:Robot, mission:Goal)->bool:
        return robot.achieve_mission(mission)