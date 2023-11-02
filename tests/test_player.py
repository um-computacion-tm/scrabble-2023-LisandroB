import unittest
from game.player import Player
from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
        self.assertEqual(len(player1.tiles), 7)

    def test_shufflinTiles(self):
        bagTiles = BagTiles()
        player1 = Player(bagTiles, id=1)
        player1.shuffleTiles()
        self.assertEqual(len(player1.tiles), 7)

    def test_getTiles(self):
        bagTiles = BagTiles()
        Player(bagTiles, id=1)
        self.assertEqual(len(bagTiles.tiles), 94)

    def test_fillTiles(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('F', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("casa", (8, 8), "V")
        self.assertEqual(len(scrabbleGame.current_player.tiles), 3)
        scrabbleGame.current_player.fillTiles(scrabbleGame.bagTiles, scrabbleGame)
        self.assertEqual(len(scrabbleGame.bagTiles.tiles), 83)
        self.assertEqual(len(scrabbleGame.current_player.tiles), 7)

    def test_fillTilesWithDoubleTurn(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('F', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("casa", (8, 8), "V")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('I', 1), 
            Tile('U', 1), 
            Tile('A', 1), 
            Tile('G', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("guias", (11, 5), "H")
        self.assertEqual(len(scrabbleGame.current_player.tiles), 3)
        scrabbleGame.current_player.fillTiles(scrabbleGame.bagTiles, scrabbleGame)
        self.assertEqual(len(scrabbleGame.bagTiles.tiles), 83)
        self.assertEqual(len(scrabbleGame.current_player.tiles), 7)
        
    def test_quitGameThroughFillTiles(self):
        scrabbleGame = ScrabbleGame(4)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('F', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("casa", (8, 8), "V")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile('X', 1), 
            Tile('S', 1), 
            Tile('I', 1), 
            Tile('U', 1), 
            Tile('A', 1), 
            Tile('G', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.putWord("guias", (11, 5), "H")
        scrabbleGame.bagTiles.tiles = []
        self.assertEqual(len(scrabbleGame.current_player.tiles), 3)
        with self.assertRaises(AssertionError):
            scrabbleGame.current_player.fillTiles(scrabbleGame.bagTiles, scrabbleGame)
    
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
        self.assertFalse(player1.hasWord("torpe"))
            
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
    
    def test_playerHasSwappedAllTiles(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()        
        scrabbleGame.current_player.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('S', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.current_player.swapTiles(scrabbleGame.bagTiles, scrabbleGame, [1, 2, 3, 4, 5, 6, 7])

    def test_playerHasSwappedSomeTiles(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile('D', 1), 
            Tile('A', 1), 
            Tile('C', 1), 
            Tile('G', 1), 
            Tile('O', 1), 
            Tile('O', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.current_player.swapTiles(scrabbleGame.bagTiles, scrabbleGame, [6, 3, 2])

    def test_playerHasSwappedOneTile(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile('A', 1), 
            Tile('A', 1), 
            Tile('F', 1), 
            Tile('E', 1), 
            Tile('A', 1), 
            Tile('S', 1), 
            Tile('I', 1)
        ]
        scrabbleGame.current_player.swapTiles(scrabbleGame.bagTiles, scrabbleGame, [1])
    
if __name__ == '__main__':
    unittest.main(buffer=True) 