from system import System
from tests import Test

DEBUG = True

'''
todo:
    -add all agents
    -create text-based UI system
    -add class to handle the analysis (system class)
        -add validation/checks to system class
    -create test class to hold all the tests (so theyre not all in main.py)

ideas:
    -recs based on map
        ex: most likely to play operator here
            becareful going hookah (your team has no drone)
    -composition overview (1 controller, 2 initiator, 1 duelist, 1 controller, etc)
    -recs based on agents
'''

def main():
    if(DEBUG):
        test = Test()
        test.test_omen()
        test.test_breach()
        test.test_chamber()
        test.test_kayo()
        test.test_sova()

    sys = System()
    sys.run()
    
if __name__ == "__main__":
    main()