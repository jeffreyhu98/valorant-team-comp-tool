from omen import Omen
from breach import Breach
from chamber import Chamber
from kayo import Kayo
from sova import Sova

DEBUG = True

'''
todo:
    -add all agents
    -create text-based UI system
    -change tests into assert statements
    -add class to handle the analysis
    -add role to agents

ideas:
    -recs based on map
        ex: most likely to play operator here
            becareful going hookah (your team has no drone)
    -composition overview (1 controller, 2 initiator, 1 duelist, 1 controller, etc)
    -recs based on agents
'''


def test_omen():
    player = Omen()
    print("---- TESTING OMEN ----")
    assert(player.smoke == 1)
    assert(player.trip == 0)
    assert(player.reconSoft == 0)
    assert(player.reconHard == 0)
    assert(player.drone == 0)
    assert(player.flash == 0)
    assert(player.nearsight == 1)
    assert(player.stun == 0)
    assert(player.operator == 0)
    assert(player.flush == 0)
    assert(player.delay == 0)

def test_breach():
    player = Breach()
    print("---- TESTING BREACH ----")
    assert(player.smoke == 0)
    assert(player.trip == 0)
    assert(player.reconSoft == 0)
    assert(player.reconHard == 0)
    assert(player.drone == 0)
    assert(player.flash == 2)
    assert(player.nearsight == 0)
    assert(player.stun == 1)
    assert(player.operator == 0)
    assert(player.flush == 1)
    assert(player.delay == 0)

def test_chamber():
    player = Chamber()
    print("---- TESTING CHAMBER ----")
    assert(player.smoke == 0)
    assert(player.trip == 1)
    assert(player.reconSoft == 0)
    assert(player.reconHard == 0)
    assert(player.drone == 0)
    assert(player.flash == 0)
    assert(player.nearsight == 0)
    assert(player.stun == 0)
    assert(player.operator == 1)
    assert(player.flush == 0)
    assert(player.delay == 0)

def test_kayo():
    player = Kayo()
    print("---- TESTING KAYO ----")
    assert(player.smoke == 0)
    assert(player.trip == 0)
    assert(player.reconSoft == 1)
    assert(player.reconHard == 0)
    assert(player.drone == 0)
    assert(player.flash == 2)
    assert(player.nearsight == 0)
    assert(player.stun == 0)
    assert(player.operator == 0)
    assert(player.flush == 1)
    assert(player.delay == 1)

def test_sova():
    player = Sova()
    print("---- TESTING SOVA ----")
    assert(player.smoke == 0)
    assert(player.trip == 0)
    assert(player.reconSoft == 0)
    assert(player.reconHard == 1)
    assert(player.drone == 1)
    assert(player.flash == 0)
    assert(player.nearsight == 0)
    assert(player.stun == 0)
    assert(player.operator == 0)
    assert(player.flush == 1)
    assert(player.delay == 0)

def main():
    if(DEBUG):
        test_omen()
        test_breach()
        test_chamber()
        test_kayo()
        test_sova()

if __name__ == "__main__":
    main()