from agent import Agent

class Breach(Agent):
    def __init__(self):
        Agent.__init__(self, "breach")
        self.flash = 2
        self.stun = 1
        self.flush = 1
