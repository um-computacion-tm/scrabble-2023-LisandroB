import unittest
from game.player import Player
from game.models import Tile, BagTiles


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 0)

    def test_validate_user_has_letters(self):
        player_1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='H', value=1),
            Tile(letter='C', value=1),
            Tile(letter='A', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player_1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        is_valid = player_1.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        player_1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='O', value=1),
            Tile(letter='U', value=1),
            Tile(letter='C', value=1),
            Tile(letter='M', value=1),
        ]
        player_1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        is_valid = player_1.has_letters(tiles)
        self.assertEqual(is_valid, False)

    def test_validate_another_fail_when_user_has_not_letters(self):
        player_1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='X', value=1),
            Tile(letter='V', value=1),
            Tile(letter='F', value=1),
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
            Tile(letter='M', value=1),
            Tile(letter='Ñ', value=1),
        ]
        player_1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile(letter='C', value=1),
            Tile(letter='A', value=1),
            Tile(letter='M', value=1),
            Tile(letter='A', value=1),
        ]
        is_valid = player_1.has_letters(tiles)
        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest.main()