import unittest
from game.models import BagTiles
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        self.assertEqual(
            len(player.tiles),
            7,
        )
        
if __name__ == '__main__':
    unittest.main()
    