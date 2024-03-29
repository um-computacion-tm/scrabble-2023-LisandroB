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
        self.turn = 0;
        for index in range(playerCount):
            self.players.append(Player(self.bagTiles, id=index+1))
        self.current_player = None

    def isWordInBoard(self, word, location, orientation):
        (x, y) = location
        if  ('í' in word or 'é' in word or 'ú' in word or 'ó' in word or 'á' in word):
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

    def iterateHorizontally(self, word, i):
        global x, y
        global res
        if self.board.getCellInBoard(x, y).tile == "":
            res += word[i]
            if not len(word) == i+1:
                x+=1
        if str(self.board.getCellInBoard(x, y).tile).lower() == word[i]:
            res += word[i]
            if not len(word) == i+1:
                x+=1

    def iterateVertically(self, word, i):
        global x, y
        global res
        if self.board.getCellInBoard(x, y).tile == "":
            res += word[i]
            if not len(word) == i+1:
                y+=1
        if str(self.board.getCellInBoard(x, y).tile).lower() == word[i]:
            res += word[i]
            if not len(word) == i+1:
                y+=1 

    def checkOrientation(self, word, orientation, i):
        global x, y
        global res
        if orientation == "V" or orientation == "v":
            self.iterateHorizontally(word, i)
        if orientation == "H" or orientation == "h":
            self.iterateVertically(word, i)

    def isInRightOrder(self, word, orientation):
        global x, y
        global res
        res = ""
        word = self.board.specialWord(word)
        for i in range(len(word)):
            self.checkOrientation(word, orientation, i)
        if res == word:
            return True;
        else:
            raise Exception("Palabra mal puesta!")

    def next_turn(self):
        if self.current_player is None:
            self.turn+=1
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]: #Accediendo al ultimo valor de la lista
            self.turn+=1
            self.current_player = self.players[0]
        else:
            self.turn+=1
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
    
    def isFirstTurn(self, word, orientation):
        global x, y
        for _ in word:
            if orientation == "V" or orientation == "v":
                if self.board.getCellInBoard(x, y) == self.board.getCellInBoard(8, 8):
                    return True
                x+=1
            elif orientation == "H" or orientation == "h":
                if self.board.getCellInBoard(x, y) == self.board.getCellInBoard(8, 8):
                    return True
                y+=1
        else:
            raise Exception("La primer palabra debe cruzar por la celda del centro! (8, 8)")

    def checkIfFirstTurn(self, word, orientation):
        global x, y
        if self.turn == 1:
            return self.isFirstTurn(word, orientation)
        elif self.turn > 1: 
            return True;

    def checkIfNextToTile(self, word, location, orientation):
        global x, y
        if not self.isNextToTile(word, location, orientation) == None:
            (x, y) = location
            return self.isInRightOrder(word, orientation)
        else:
            raise Exception("Palabra debe continuar con las del tablero!")
    
    def CheckVertOrHoriTiles(self, _, location, orientation):
        global x, y
        if orientation == "V" or orientation == "v":
            if str(self.board.getCellInBoard(x, y).tile).lower() == _:
                return True;
            if self.board.getCellInBoard(x, y).tile == "":
                x+=1
            else:
                pass;
        if orientation == "H" or orientation == "h":
            if str(self.board.getCellInBoard(x, y).tile).lower() == _:
                return True;
            if self.board.getCellInBoard(x, y).tile == "":
                y+=1
            else:
                pass;
    
    def verticalOrHorizontalTile(self, word, location, orientation):
        global x, y
        (x, y) = location
        for _ in word:
            if self.CheckVertOrHoriTiles(_, location, orientation):
                return True;
    
    def isNextToTile(self, word, location, orientation):
        global x, y
        if self.turn > 1:
            for _ in word:
                if self.verticalOrHorizontalTile(word, location, orientation):
                    return True;
        else:
            return True;

    def ifPlayerHasWordAndFitsInBoard(self, word, location, orientation):
        global x, y
        if (self.current_player.hasWord(word) and self.board.validate_word_inside_board(word, location, orientation)):
            return True
        else:
            return False;

    def ifWordIsInBoardAndFits(self, word, location, orientation):
        global x, y
        if (self.isWordInBoard(word, location, orientation) and self.board.validate_word_inside_board(word, location, orientation)):
            return True;
        else:
            return False;

    def validateWord(self, word, orientation):
        global x, y
        location = (x, y)
        if (self.ifPlayerHasWordAndFitsInBoard(word, location, orientation) and dict(word) and self.checkIfFirstTurn(word, orientation)):
            return self.checkIfNextToTile(word, location, orientation)
        elif (self.ifWordIsInBoardAndFits(word, location, orientation) and dict(word) and self.checkIfFirstTurn(word, orientation)):
            return self.checkIfNextToTile(word, location, orientation)

    def addOneTileAppendScoreMoveOnePosRemovePlayerTile(self, orientation, i):
        global x, y
        if orientation == "V" or orientation == "v":
            self.board.addTileToCell(x, y, Tile(self.current_player.tiles[i].letter, self.current_player.tiles[i].value))
            self.score.append(self.board.getCellInBoard(x, y))
            x+=1
            self.current_player.tiles.pop(i)
        elif orientation == "H" or orientation == "h":
            self.board.addTileToCell(x, y, Tile(self.current_player.tiles[i].letter, self.current_player.tiles[i].value))
            self.score.append(self.board.getCellInBoard(x, y))
            y+=1
            self.current_player.tiles.pop(i)

    def scoreMove(self, orientation):
        global x, y
        if orientation == "V" or orientation == "v":
            self.score.append(self.board.getCellInBoard(x, y))
            x+=1
            return x
        elif orientation == "H" or orientation == "h":
            self.score.append(self.board.getCellInBoard(x, y))
            y+=1
            return y
        
    def formWord(self, word, orientation):
        global x, y
        for letter in word:
            for i in range(len(self.current_player.tiles)): 
                letter = self.board.isSpecial(letter)
                if (letter == str(self.board.getCellInBoard(x, y)).lower() and letter == self.current_player.tiles[i].letter.lower()):
                    self.scoreMove(orientation)
                    break;
                if letter == str(self.board.getCellInBoard(x, y)).lower():
                    self.scoreMove(orientation)
                    break;
                if (letter == self.current_player.tiles[i].letter.lower() or letter == str(self.board.getCellInBoard(x, y)).lower()):
                    self.addOneTileAppendScoreMoveOnePosRemovePlayerTile(orientation, i)
                    break;
        
    def putWord(self, word, location, orientation):
        self.score = []
        global x, y
        (x, y) = location
        if self.validateWord(word, orientation):
            (x, y) = location
            word = [char for char in word]
            self.formWord(word, orientation)
            self.current_player.score += self.board.calculateWordValue(self.score)
            return True