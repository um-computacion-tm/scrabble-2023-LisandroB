import unittest;
from game.cli import Game

class testCli(unittest.TestCase):
    def test_showBoard(self):
        game = Game()
        game.showBoard()

if __name__ == '__main__':
    unittest.main()