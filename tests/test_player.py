import unittest
from game.player import Player
from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
        self.assertEqual(len(player1.tiles), 7)

    def test_getTiles(self):
        bagTiles = BagTiles()
        Player(bagTiles, id=1)
        self.assertEqual(len(bagTiles.tiles), 94)

    def test_fillTiles(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('F', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("casa", (3, 2), "V")
        self.assertEqual(len(scrabbleGame.current_player.tiles), 3)
        scrabbleGame.current_player.fillTiles(scrabbleGame.bagTiles)
        self.assertEqual(len(scrabbleGame.bagTiles.tiles), 83)
        self.assertEqual(len(scrabbleGame.current_player.tiles), 7)

    def test_fillTilesWithDoubleTurn(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('F', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("casa", (3, 2), "V")
        scrabbleGame.current_player.fillTiles(scrabbleGame.bagTiles)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.current_player.tiles = [
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('I', 1), 
            Tile('U', 1), 
            Tile('A', 1), 
            Tile('G', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("guias", (7, 3), "H")
        self.assertEqual(len(scrabbleGame.current_player.tiles), 2)
        scrabbleGame.current_player.fillTiles(scrabbleGame.bagTiles)
        self.assertEqual(len(scrabbleGame.bagTiles.tiles), 78)
        self.assertEqual(len(scrabbleGame.current_player.tiles), 7)
        
    def test_playerHasWord(self):
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
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
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
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
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
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
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
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

    def test_validate_user_has_letters(self):
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
        bagTiles.tiles = [
            Tile('O', 1),
            Tile('L', 1),
            Tile('H', 1),
            Tile('C', 1),
            Tile('A', 1),
            Tile('U', 1),
            Tile('M', 1)
        ]
        player1.tiles.extend(bagTiles.tiles)
        tiles = [
            Tile('H', 1),
            Tile('O', 1),
            Tile('L', 1),
            Tile('A', 1)
        ]
        is_valid = player1.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_user_has_letters2(self):
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
        bagTiles.tiles = [
            Tile('O', 1),
            Tile('A', 1),
            Tile('F', 1),
            Tile('V', 1),
            Tile('A', 1),
            Tile('I', 1),
            Tile('N', 1)
        ]
        player1.tiles.extend(bagTiles.tiles)
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