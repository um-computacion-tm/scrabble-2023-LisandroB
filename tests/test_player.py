import unittest
from game.models import BagTiles
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(BagTiles.getTiles())
        self.assertEqual(
            len(player_1),
            7,
        )

if __name__ == '__main__':
    unittest.main()
