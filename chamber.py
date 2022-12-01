from agent import Agent

class Chamber(Agent):
    def __init__(self):
        Agent.__init__(self, "chamber")
        self.trip = 1
        self.operator = 1
