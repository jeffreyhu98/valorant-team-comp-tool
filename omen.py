from agent import Agent

class Omen(Agent):
    def __init__(self):
        Agent.__init__(self, "omen")
        self.smoke = 1
        self.nearsight = 1
