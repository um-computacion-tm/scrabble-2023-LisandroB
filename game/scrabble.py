from game.board import Board
from game.player import Player
from game.models import BagTiles, Tile
from game.dictionary import validate_word as dict

class ScrabbleGame:
    def __init__(self, playerCount: int):
        self.board = Board()
        self.bagTiles = BagTiles()
        self.players:list[Player] = []
        for index in range(playerCount):
            self.players.append(Player(self.bagTiles, id=index+1))
        self.current_player = None

    def validateTurn(self, word, location, orientation):
        if len(self.bagTiles.tiles) > 0:
            return self.putWord(word, location, orientation)
        else:
            return False;

    def getScore(self):
        print("------------------------ Scoreboard ------------------------")
        for _ in self.players:
            print(f"Player {_.id}: {_.score}")
        return True;

    def removeTileFromPlayer(self, index):
        self.current_player.tiles.pop(index)

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
    
    def putWord(self, word, location, orientation):
        (x, y) = location
        if self.validateWord(word, location, orientation):
            word = [char for char in word]
            score = []
            ## parse current_player's letters and values from its tiles 
            ## search tiles that match word's letters
            ## add found tiles to cells in specific directions and length
            for _ in word:
                for i in range(len(self.current_player.tiles)):
                    if _ == self.current_player.tiles[i].letter.lower():
                        if orientation == "V" or orientation == "v":
                            self.board.addTileToCell(x, y, Tile(
                                self.current_player.tiles[i].letter,
                                self.current_player.tiles[i].value
                            ))
                            score.append(self.board.getCellInBoard(x, y))
                            x+=1
                            self.removeTileFromPlayer(i)
                            break;
                        elif orientation == "H" or orientation == "h":
                            self.board.addTileToCell(x, y, Tile(
                                self.current_player.tiles[i].letter,
                                self.current_player.tiles[i].value
                            ))
                            score.append(self.board.getCellInBoard(x, y))
                            y+=1
                            self.removeTileFromPlayer(i)
                            break;
            self.current_player.score = self.board.calculateWordValue(score)
            return True;
        else:
            return False;