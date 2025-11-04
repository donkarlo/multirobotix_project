from typing import Optional, List, Tuple

from robotix.experiment.scenario import Scenario as BaseScenario
from robotix.mind.action.composite.plan.plan import Plan
from robotix.mind.goal.composite.mission.mission import Mission
from robotix.robot import Robot
from physix.world.world import World


class Scenario(BaseScenario):
    """
    Scenario is more than a robot and its missions
    For ecxample it might include the world mission_state such as walls
    """

    def __init__(self, robots_missions_plans:List[Tuple[Robot,Mission,Plan]], world: World, label: Optional[str] = None):
        """

        Args:
            robots_missions_plans:
            world:
            label:
        """
        self._robots_missions_plans = robots_missions_plans

        self._world = world
        self._name = label

        # run

    def run(self) -> None:
        for robot, mission, _ in self._robots_missions_plans:
            robot.achieve_mission(mission)

    def remember(self):
        self._robot.remember()

    def get_world(self) -> World:
        return self._world

    def get_mission(self, robot_name:str) -> Mission:
        for robot, mission, plan in self._robots_missions_plans:
            if robot.get_name() == robot_name:
                return mission

    def get_robots(self) -> List[Robot]:
        robots = []
        for robot, mission, plan in self._robots_missions_plans:
            robots.append(robot)
        return robots

    def get_plan(self, robot_name: str) -> Robot:
        for robot, mission, plan in self._robots_missions_plans:
            if robot.get_name() == robot_name:
                return plan

    def get_name(self) -> Optional[str]:
        return self._name