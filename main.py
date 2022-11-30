from omen import Omen

def test_omen():
    player = Omen()
    print("[",player.smoke,"]", "expected: 1")
    print("[",player.drone,"]", "expected: 0")
    print("[",player.wall,"]", "expected: 0")
    print("[",player.trip,"]", "expected: 0")
    print("[",player.reconSoft,"]", "expected: 0")
    print("[",player.reconHard,"]", "expected: 0")
    print("[",player.drone,"]", "expected: 0")
    print("[",player.flash,"]", "expected: 0")
    print("[",player.nearsight,"]", "expected: 1")
    print("[",player.stun,"]", "expected: 0")
    print("[",player.operator,"]", "expected: 0")

def main():
    test_omen()

if __name__ == "__main__":
    main()