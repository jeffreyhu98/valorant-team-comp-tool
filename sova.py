from agent import Agent

class Sova(Agent):
    def __init__(self):
        Agent.__init__(self, "sova")
        self.reconHard = 1
        self.drone = 1
        self.flush = 1
