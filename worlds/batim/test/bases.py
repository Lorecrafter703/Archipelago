from test.bases import WorldTestBase

from ..world import BATIMWorld


class BATIMTestBase(WorldTestBase):
    game = "Bendy and the Ink Machine"
    world: BATIMWorld
