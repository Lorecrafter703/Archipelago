from .bases import BATIMTestBase

class TestBasics(BATIMTestBase):
    options = {
        "total_bacon_soups": 0,
        "bacon_soups_required": 0,
    }

    def test_no_bacon_soups(self) -> None:
        ch5 = self.world.get_region("CH5")

        self.assertTrue(ch5.can_reach(self.multiworld.state))