from role import Role

class Agent:
    def __init__(self, name):
        self.name = name
        self.role = 0
        self.smoke = 0
        self.trip = 0
        self.reconSoft = 0
        self.reconHard = 0
        self.drone = 0
        self.flash = 0
        self.nearsight = 0
        self.stun = 0
        self.operator = 0
        self.flush = 0                  #nade, molly, aftershock, shock dart
        self.delay = 0                  #slow, sagewall, pull, molly, nade, seize
