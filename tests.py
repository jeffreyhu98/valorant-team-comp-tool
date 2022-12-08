from role import Role
from agents.omen import Omen
from agents.breach import Breach
from agents.chamber import Chamber
from agents.kayo import Kayo
from agents.sova import Sova

class Test():

    def __init__(self) -> None:
        pass

    def test_omen(self):
        player = Omen()
        print("---- TESTING OMEN ----")
        assert(player.role == Role.CONTROLLER)
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

    def test_breach(self):
        player = Breach()
        print("---- TESTING BREACH ----")
        assert(player.role == Role.INITIATOR)
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

    def test_chamber(self):
        player = Chamber()
        print("---- TESTING CHAMBER ----")
        assert(player.role == Role.SENTINEL)
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

    def test_kayo(self):
        player = Kayo()
        print("---- TESTING KAYO ----")
        assert(player.role == Role.INITIATOR)
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

    def test_sova(self):
        player = Sova()
        print("---- TESTING SOVA ----")
        assert(player.role == Role.INITIATOR)
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