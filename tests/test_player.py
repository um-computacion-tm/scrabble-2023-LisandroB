import unittest
from game.models import BagTiles
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
<<<<<<< HEAD
        player_1 = Player(BagTiles)
=======
        player_1 = Player(BagTiles="BagTiles")
>>>>>>> dc62c1b6d28c455f3387ee94d8bec11b3887d0fc
        self.assertEqual(
            len(player_1.BagTiles),
            0,
        )

if __name__ == '__main__':
    unittest.main()
