from agent import Agent
from role import Role

class Fade(Agent):
    def __init__(self):
        Agent.__init__(self, "fade")
        self.role = Role.INITIATOR
        self.reconHard = 1
        self.drone = 1
        self.nearsight = 1
        self.delay = 1
