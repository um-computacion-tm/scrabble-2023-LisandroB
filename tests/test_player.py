import unittest
from game.player import Player
from game.models import Tile, BagTiles

""" 
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 0)

    def test_validate_user_has_letters(self):
        player_1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = player_1.tiles
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)

        def test_validate_fail_when_user_has_not_letters(self):
            bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = player(bagTile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest.main()
"""
