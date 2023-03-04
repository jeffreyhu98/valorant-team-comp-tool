from agent import Agent
from role import Role

class Viper(Agent):
    def __init__(self):
        Agent.__init__(self, "viper")
        self.role = Role.CONTROLLER
        self.smoke = 1
        self.flush = 2
        self.delay = 2
