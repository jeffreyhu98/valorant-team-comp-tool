from agent import Agent
from role import Role

class Sova(Agent):
    def __init__(self):
        Agent.__init__(self, "sova")
        self.role = Role.INITIATOR
        self.reconHard = 1
        self.drone = 1
        self.flush = 1
