import unittest
from game.player import Player
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player1 = Player()
        self.assertEqual(len(player1.tiles), 0)
    
    def test_rellenar(self):
        player1 = Player()
        player1.getTiles()
        self.assertEqual(len(player1.tiles), 7)

    def test_playerHasWord(self):
        player1 = Player()
        player1.tiles = [Tile('A', 1), Tile('A', 1), Tile('C', 1), Tile('X', 1), Tile('S', 1), Tile('F', 1), Tile('I', 1)]
        self.assertEqual(player1.hasWord("casa"), True)

    def test_playerDoesntHaveWord(self):
        player1 = Player()
        player1.tiles = [Tile('T', 1), Tile('C', 1), Tile('E', 1), Tile('A', 1), Tile('D', 1), Tile('O', 1), Tile('D', 1)]
        self.assertEqual(player1.hasWord("torpe"), False)
    
    def test_playerHasNoTiles(self):
        player1 = Player()
        self.assertEqual(player1.hasWord("torpe"), False)

    def test_validate_user_has_letters(self):
        player1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='H', value=1),
            Tile(letter='C', value=1),
            Tile(letter='A', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1)
        ]
        player1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1)
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_user_has_letters2(self):
        player1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='O', value=1),
            Tile(letter='A', value=1),
            Tile(letter='F', value=1),
            Tile(letter='V', value=1),
            Tile(letter='A', value=1),
            Tile(letter='I', value=1),
            Tile(letter='N', value=1)
        ]
        player1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile(letter='A', value=1),
            Tile(letter='V', value=1),
            Tile(letter='I', value=1),
            Tile(letter='O', value=1),
            Tile(letter='N', value=1)
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        player1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='O', value=1),
            Tile(letter='U', value=1),
            Tile(letter='C', value=1),
            Tile(letter='M', value=1)
        ]
        player1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1)
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, False)

    def test_validate_another_fail_when_user_has_not_letters(self):
        player1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile(letter='X', value=1),
            Tile(letter='V', value=1),
            Tile(letter='F', value=1),
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
            Tile(letter='M', value=1),
            Tile(letter='Ñ', value=1)
        ]
        player1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile(letter='C', value=1),
            Tile(letter='A', value=1),
            Tile(letter='M', value=1),
            Tile(letter='A', value=1)
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest.main()