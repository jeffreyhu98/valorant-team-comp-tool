from agent import Agent
from role import Role

class Breach(Agent):
    def __init__(self):
        Agent.__init__(self, "breach")
        self.role = Role.INITIATOR
        self.flash = 2
        self.stun = 1
        self.flush = 1
