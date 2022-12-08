from agent import Agent
from role import Role

class Reyna(Agent):
    def __init__(self):
        Agent.__init__(self, "reyna")
        self.role = Role.DUELIST
        self.nearsight = 1
        
