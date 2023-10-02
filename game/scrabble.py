from game.board import Board
from game.player import Player
from game.models import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
    def calculate_word_value(word):
        result = 0;
        mulres = 0; ## creating a variable for adding whatever the _.multiplier throws back 
        for _ in word:
            if _.multiplier_type=="letter":
                result += _.letter.value * _.multiplier
            elif _.multiplier == None or _.multiplier_type == None:
                result += _.letter.value 
            elif _.multiplier_type=="word":
                mulres = _.multiplier
                            
        return result;