from agent import Agent
from role import Role

class Omen(Agent):
    def __init__(self):
        Agent.__init__(self, "omen")
        self.role = Role.CONTROLLER
        self.smoke = 1
        self.nearsight = 1
