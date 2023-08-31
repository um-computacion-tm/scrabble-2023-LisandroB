from game.board import Board
from game.player import Player
from game.models import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count, 4):
            self.players.append(Player(BagTiles="BagTiles"))
    def calculate_word_value(self, word):
        result = 0;
        for _ in range(len(word)):
            result =+ word.Cell.letter[1]
        return result;