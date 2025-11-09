from typing import List

from multirobotix.group import Group as BaseRobotGroup
from multirobotix.homogeneity.homogeneities import Homogeneities
from robotix.robot import Robot


class LeaderFollowers(BaseRobotGroup):
    def __init__(self, leader:Robot, followers:List[Robot], homogeneity:Homogeneities):
        self._leader = leader
        self._followers = followers
        all_robots = [self._leader]+self._followers
        super().__init__(all_robots, homogeneity)

    def get_leader(self) -> Robot:
        return self._leader
    def get_followers(self) -> List[Robot]:
        return self._followers
