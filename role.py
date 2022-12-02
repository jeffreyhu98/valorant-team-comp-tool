from enum import Enum

'''
    enum of all agent types;
    handled by role attribute in Agent class
'''
class Role(Enum):
    CONTROLLER = 1
    INITIATOR = 2
    DUELIST = 3
    SENTINEL = 4