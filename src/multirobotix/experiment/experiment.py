from robotix.experiment.experiment import Experiment as RoboticExperiment


class Experiment(RoboticExperiment):
    def __init__(self):
        self._robots = []