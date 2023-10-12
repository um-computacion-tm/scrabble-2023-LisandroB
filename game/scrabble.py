from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import validate_word as dict

class ScrabbleGame:
    def __init__(self, playerCount: int):
        self.board = Board()
        self.bagTiles = BagTiles()
        self.players:list[Player] = []
        for index in range(playerCount):
            self.players.append(Player())
        self.current_player = None

    def validateTurn(self, word, location, orientation):
        ## loop through x, y coordinates if v/h, [tiles from player?] place each tile with letter and points to board
        pass;

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]: #Accediendo al ultimo valor de la lista
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def validateWord(self, word, location, orientation):
        if self.current_player.hasWord(word) and self.board.validate_word_inside_board(word, location, orientation) and dict(word):
            return True;
        else:
            return False;
    
    def get_words():
            '''
            Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
            Preguntar al usuario, por cada una de esas palabras, las que considera reales
            '''
    
    def putWords(self, word, location, orientation):
        word = [char for char in word]
        if self.validateWord(word, location, orientation):
            ## parse current_player's letters and values from its tiles 
            ## search tiles that match word's letters
            ## add found tiles to cells in specific directions and length
            (x, y) = location
            if orientation == "V":
                for _ in word:
                    self.board.addTileToCell(x, y, self.current_player.tiles)
                    y+1