from typing import Protocol, runtime_checkable, List

from robotix.mind.goal.composite.mission.mission import Mission
from robotix.robot import Robot


@runtime_checkable
class Interface(Protocol):
    _memebers:List[Robot]
    def get_memebers(self) -> List[Robot]: ...
    def achieve_mission(self, robot:Robot, mission:Mission)->bool: ...