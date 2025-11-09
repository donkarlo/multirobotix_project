from multirobotix.group import Group
from robotix.robot import Robot
from typing import List, Optional
import copy

class CollectionGenerator:
    def get_robots_by_sample(self, sample_robot: Robot, names:Optional[List[str]]=None)->Group:
        """

        Args:
            names:

        Returns:

        """
        robots = []
        self._names = names
        for counter, name in enumerate(self._names):
            # TODO: check uniqness of the __name
            copied_robot = copy.deepcopy(sample_robot)
            copied_robot.set_name(name)
            robots.append(copied_robot)
        return Group(robots)

