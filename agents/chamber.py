from agent import Agent
from role import Role

class Chamber(Agent):
    def __init__(self):
        Agent.__init__(self, "chamber")
        self.role = Role.SENTINEL
        self.trip = 1
        self.operator = 1
