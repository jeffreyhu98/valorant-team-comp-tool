from agent import Agent

class Kayo(Agent):
    def __init__(self):
        Agent.__init__(self, "kayo")
        self.reconSoft = 1
        self.flash = 2
        self.flush = 1
        self.delay = 1
