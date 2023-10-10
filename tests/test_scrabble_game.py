import unittest
from game.scrabble import ScrabbleGame

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        self.assertIsNotNone(scrabbleGame.board)
        self.assertEqual(len(scrabbleGame.players), 3)
        self.assertIsNotNone(scrabbleGame.bagTiles)
    
    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[0]
    
    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 4 jugadores, luego del jugador 3, le toca al jugador 4
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[3]
    
    def test_validateWordRight(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        self.assertEqual(scrabbleGame.validateWord("papa", (8, 7), "V"), True)
        
    def test_validateWordRight(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[0]
        self.assertEqual(scrabbleGame.validateWord("empanada", (15, 7), "H"), False)
    
if __name__ == '__main__':
    unittest.main()