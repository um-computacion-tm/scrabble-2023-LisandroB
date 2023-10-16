import unittest
from game.player import Player
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player1 = Player()
        self.assertEqual(len(player1.tiles), 7)

    def test_playerHasWord(self):
        player1 = Player()
        player1.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('F', 1), 
            Tile('I', 1)
        ]
        self.assertEqual(player1.hasWord("casa"), True)

    def test_playerDoesntHaveWord(self):
        player1 = Player()
        player1.tiles = [
            Tile('T', 1), 
            Tile('C', 1), 
            Tile('E', 1), 
            Tile('A', 1), 
            Tile('D', 1), 
            Tile('O', 1), 
            Tile('D', 1)
        ]
        self.assertEqual(player1.hasWord("torpe"), False)
    
    def test_playerAlmostHasWord(self):
        player1 = Player()
        player1.tiles = [
            Tile('T', 1), 
            Tile('C', 1), 
            Tile('P', 1), 
            Tile('A', 1), 
            Tile('D', 1), 
            Tile('O', 1), 
            Tile('R', 1)
        ]
        self.assertEqual(player1.hasWord("torpe"), False)

    def test_playerHasWordWithMoreTiles(self):
        player1 = Player()
        player1.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('S', 1), 
            Tile('I', 1)
        ]
        self.assertEqual(player1.hasWord("casa"), True)
    
    def test_playerHasNoTiles(self):
        player1 = Player()
        self.assertEqual(player1.hasWord("torpe"), False)

    def test_validate_user_has_letters(self):
        player1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile('O', 1),
            Tile('L', 1),
            Tile('H', 1),
            Tile('C', 1),
            Tile('A', 1),
            Tile('U', 1),
            Tile('M', 1)
        ]
        player1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1)
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_user_has_letters2(self):
        player1 = Player()
        bagTile = BagTiles()
        bagTile.tiles = [
            Tile('O', 1),
            Tile('A', 1),
            Tile('F', 1),
            Tile('V', 1),
            Tile('A', 1),
            Tile('I', 1),
            Tile('N', 1)
        ]
        player1.tiles.extend(bagTile.tiles)
        tiles = [
            Tile('A', 1),
            Tile('V', 1),
            Tile('I', 1),
            Tile('O', 1),
            Tile('N', 1)
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, True)

if __name__ == '__main__':
    unittest.main()