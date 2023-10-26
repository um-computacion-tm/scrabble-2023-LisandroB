from game.board import Board
from game.player import Player
from game.models import BagTiles, Tile
from game.dictionary import validate_word as dict
from unidecode import unidecode

class ScrabbleGame:
    def __init__(self, playerCount: int):
        self.board = Board()
        self.bagTiles = BagTiles()
        self.players:list[Player] = []
        self.score = []
        for index in range(playerCount):
            self.players.append(Player(self.bagTiles, id=index+1))
        self.current_player = None
    
    def isWordInBoard(self, word, location, orientation):
        (x, y) = location
        if  (
                'í' in word 
                or 'é' in word 
                or 'ú' in word 
                or 'ó' in word 
                or 'á' in word
            ):
                word = unidecode(word)
        cellsInBoard = []
        playerTiles = []
        result = []
        for _ in self.current_player.tiles:
            playerTiles.append(_.letter.lower())

        for _ in word:
            if orientation == "V" or orientation == "v":
                cellsInBoard.append(str(self.board.getCellInBoard(x, y)))
                x+=1
            elif orientation == "H" or orientation == "h":
                cellsInBoard.append(str(self.board.getCellInBoard(x, y)))
                y+=1
        
        for _ in word:
            if _ in cellsInBoard or _ in playerTiles:
                result.append(_)
                if _ in playerTiles:
                    playerTiles.pop(playerTiles.index(_))
        
        if ''.join(result) == word:
            return True;
        else:
            raise Exception("Palabra no está en tablero!")

    def validateTurn(self, word, location, orientation):
        if len(self.bagTiles.tiles) > 0:
            return self.putWord(word, location, orientation)
        else:
            raise Exception("Turno inválido!")

    def getScore(self):
        print("------------------------ Scoreboard ------------------------")
        for _ in self.players:
            print(f"Player {_.id}: {_.score}")

    def removeTileFromPlayer(self, index):
        self.current_player.tiles.pop(index)
    
    def addScore(self, x, y):
        self.score.append(self.board.getCellInBoard(x, y))

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]: #Accediendo al ultimo valor de la lista
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def validateWord(self, word, location, orientation):
        if (
            self.current_player.hasWord(word)
            and self.board.validate_word_inside_board(word, location, orientation)
            and dict(word)
        ):
            word = unidecode(word)
            return True;
        elif (
            self.isWordInBoard(word, location, orientation)
            and
            self.board.validate_word_inside_board(word, location, orientation)
            and
            dict(word)
        ):
            word = unidecode(word)
            return True;

    def checkIfWordAlreadyThere(self, orientation, letter, i, location):
        (x, y) = location
        if (letter == str(self.board.getCellInBoard(x, y)).lower()
            and letter == self.current_player.tiles[i].letter.lower()):
            return self.addScoreThenMoveOneTile(x, y, orientation)
        if letter == str(self.board.getCellInBoard(x, y)).lower():
            return self.addScoreThenMoveOneTile(x, y, orientation)

    def moveOneTile(self, xy):
        return xy + 1

    def addScoreThenMoveOneTile(self, x, y, orientation):
        self.addScore(x, y)
        if orientation == "V" or orientation == "v":
            return self.moveOneTile(x)
        elif orientation == "H" or orientation == "h":
            return self.moveOneTile(y)

    def addMultipleTilesToCellAddScoreRemoveTile(self, x, y, i, orientation):
        self.board.addTileToCell(x, y, Tile(
            self.current_player.tiles[i].letter,
            self.current_player.tiles[i].value
            )
        )
        self.removeTileFromPlayer(i)
        return self.addScoreThenMoveOneTile(x, y, orientation)

    def checkIfNonUnicode(self, word):
        if ('í' in word or 'é' in word or 'ú' in word or 'ó' in word or 'á' in word):
            word = unidecode(word)

    def putWord(self, word, location, orientation):
        (x, y) = location
        if self.validateWord(word, location, orientation):
            self.checkIfNonUnicode(word)
            word = [char for char in word]
            for letter in word:
                for i in range(len(self.current_player.tiles)):             
                    self.checkIfWordAlreadyThere(orientation, letter, i, location)
                    if (
                        letter == self.current_player.tiles[i].letter.lower()
                        or letter == str(self.board.getCellInBoard(x, y)).lower()
                    ):
                        if orientation == "V" or orientation == "v":
                            x = self.addMultipleTilesToCellAddScoreRemoveTile(x, y, i, orientation)
                            break;
                        elif orientation == "H" or orientation == "h":
                            y = self.addMultipleTilesToCellAddScoreRemoveTile(x, y, i, orientation)
                            break;
            self.current_player.score += self.board.calculateWordValue(self.score)
            return True;