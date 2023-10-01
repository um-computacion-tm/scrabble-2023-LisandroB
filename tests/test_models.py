import unittest
from game.models import (
    BagTiles,
    Tile,
)
global bag 
bag = BagTiles()
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        s = BagTiles()
        s.getTiles()
        self.assertEqual(
            len(s.tiles),
            7,
        )

    def test_take(self):
        bag = BagTiles()
        bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            5,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            2,
        )

if __name__ == '__main__':
    unittest.main()

print(bag.tiles)