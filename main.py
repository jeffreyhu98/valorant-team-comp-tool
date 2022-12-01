from omen import Omen
from breach import Breach
from chamber import Chamber
from kayo import Kayo
from sova import Sova

'''
todo:
    -add all agents
    -create text-based UI system
    -change tests into assert statements

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
    print("[",player.smoke,"]", "expected: 1")
    print("[",player.trip,"]", "expected: 0")
    print("[",player.reconSoft,"]", "expected: 0")
    print("[",player.reconHard,"]", "expected: 0")
    print("[",player.drone,"]", "expected: 0")
    print("[",player.flash,"]", "expected: 0")
    print("[",player.nearsight,"]", "expected: 1")
    print("[",player.stun,"]", "expected: 0")
    print("[",player.operator,"]", "expected: 0")
    print("[",player.flush,"]", "expected: 0")
    print("[",player.delay,"]", "expected: 0")

def test_breach():
    player = Breach()
    print("---- TESTING BREACH ----")
    print("[",player.smoke,"]", "expected: 0")
    print("[",player.trip,"]", "expected: 0")
    print("[",player.reconSoft,"]", "expected: 0")
    print("[",player.reconHard,"]", "expected: 0")
    print("[",player.drone,"]", "expected: 0")
    print("[",player.flash,"]", "expected: 2")
    print("[",player.nearsight,"]", "expected: 0")
    print("[",player.stun,"]", "expected: 1")
    print("[",player.operator,"]", "expected: 0")
    print("[",player.flush,"]", "expected: 1")
    print("[",player.delay,"]", "expected: 0")

def test_chamber():
    player = Chamber()
    print("---- TESTING CHAMBER ----")
    print("[",player.smoke,"]", "expected: 0")
    print("[",player.trip,"]", "expected: 1")
    print("[",player.reconSoft,"]", "expected: 0")
    print("[",player.reconHard,"]", "expected: 0")
    print("[",player.drone,"]", "expected: 0")
    print("[",player.flash,"]", "expected: 0")
    print("[",player.nearsight,"]", "expected: 0")
    print("[",player.stun,"]", "expected: 0")
    print("[",player.operator,"]", "expected: 1")
    print("[",player.flush,"]", "expected: 0")
    print("[",player.delay,"]", "expected: 0")

def test_kayo():
    player = Kayo()
    print("---- TESTING KAYO ----")
    print("[",player.smoke,"]", "expected: 0")
    print("[",player.trip,"]", "expected: 0")
    print("[",player.reconSoft,"]", "expected: 1")
    print("[",player.reconHard,"]", "expected: 0")
    print("[",player.drone,"]", "expected: 0")
    print("[",player.flash,"]", "expected: 2")
    print("[",player.nearsight,"]", "expected: 0")
    print("[",player.stun,"]", "expected: 0")
    print("[",player.operator,"]", "expected: 0")
    print("[",player.flush,"]", "expected: 1")
    print("[",player.delay,"]", "expected: 1")

def test_sova():
    player = Sova()
    print("---- TESTING SOVA ----")
    print("[",player.smoke,"]", "expected: 0")
    print("[",player.trip,"]", "expected: 0")
    print("[",player.reconSoft,"]", "expected: 0")
    print("[",player.reconHard,"]", "expected: 1")
    print("[",player.drone,"]", "expected: 1")
    print("[",player.flash,"]", "expected: 0")
    print("[",player.nearsight,"]", "expected: 0")
    print("[",player.stun,"]", "expected: 0")
    print("[",player.operator,"]", "expected: 0")
    print("[",player.flush,"]", "expected: 1")
    print("[",player.delay,"]", "expected: 0")

def main():
    test_omen()
    test_breach()
    test_chamber()
    test_kayo()
    test_sova()

if __name__ == "__main__":
    main()