class Agent:
    def __init__(self, name):
        self.name = name
        self.smoke = 0
        self.trip = 0
        self.reconSoft = 0
        self.reconHard = 0
        self.drone = 0
        self.flash = 0
        self.nearsight = 0
        self.stun = 0
        self.operator = 0
        self.aoe = 0                    #nade, molly, sieze, pull
        self.delay = 0                  #slow, sagewall, pull
