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
    
    def endGame(self):
        print("Juego terminado!")
        print("Puntaje final: ")
        playersAndScores = []
        for _ in self.players:
            s = _.id, _.score
            playersAndScores.append(s)
        playersAndScores = sorted(playersAndScores, key=lambda x: x[1], reverse=True)
        for _ in playersAndScores:
            print(f"Jugador {_[0]}: {_[1]}")
        print(f"El ganador es: Jugador {playersAndScores[0][0]}")
        print("Gracias por jugar, hasta pronto!")
        raise AssertionError

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

    def validateTurn(self):
        if len(self.bagTiles.tiles) > 0 and len(self.current_player.tiles) > 0:
            return True;
        elif len(self.current_player.tiles) == 0 or len(self.bagTiles.tiles) == 0:
            self.endGame()

    def getScore(self):
        print("------------------------ Scoreboard ------------------------".center(65))
        for _ in self.players:
            print(f"Jugador {_.id}: {_.score}".center(65))

    def removeTileFromPlayer(self, index):
        self.current_player.tiles.pop(index)

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

    def checkIfNextToTile(self, word, orientation):
        global x, y
        if not self.isNextToTile(word, orientation) == None:
            return True;
        else:
            raise Exception("Palabra debe continuar con las del tablero!")

    def verticalOrHorizontalTile(self, orientation):
        global x, y
        if orientation == "V" or orientation == "v":
            if self.board.getCellInBoard(x, y).tile == "":
                x+=1
            else:
                return True;
        if orientation == "H" or orientation == "h":
            if self.board.getCellInBoard(x, y).tile == "":
                y+=1
            else:
                return True;

    def isNextToTile(self, word, orientation):
        global x, y
        if self.turn > 1:
            for _ in word:
                if self.verticalOrHorizontalTile(orientation):
                    return True;
        else:
            return True;

    def ifPlayerHasWordAndFitsInBoard(self, word, location, orientation):
        global x, y
        if (self.current_player.hasWord(word)
            and 
            self.board.validate_word_inside_board(word, location, orientation)):
            return True
        else:
            return False;

    def ifWordIsInBoardAndFits(self, word, location, orientation):
        global x, y
        if (self.isWordInBoard(word, location, orientation)
            and
            self.board.validate_word_inside_board(word, location, orientation)):
            return True;
        else:
            return False;

    def validateWord(self, word, orientation):
        global x, y
        location = (x, y)
        if (
            self.ifPlayerHasWordAndFitsInBoard(word, location, orientation)
            and 
            dict(word)
            and
            self.checkIfFirstTurn(word, orientation)
        ):
            return self.checkIfNextToTile(word,  orientation)
        elif (
            self.ifWordIsInBoardAndFits(word, location, orientation)
            and
            dict(word)
            and
            self.checkIfFirstTurn(word, orientation)
        ):
            return self.checkIfNextToTile(word, orientation)

    def isSpecial(self, letter):
        if (
            letter == "ú" 
            or letter == "é" 
            or letter == "í"
            or letter == "ó"
            or letter == "á"
        ):
            letter = unidecode(letter)
            return letter
        else:
            return letter
    
    def addOneTileAppendScoreMoveOnePosRemovePlayerTile(self, orientation, i):
        global x, y
        if orientation == "V" or orientation == "v":
            self.board.addTileToCell(x, y, Tile(
                self.current_player.tiles[i].letter,
                self.current_player.tiles[i].value
            ))
            self.score.append(self.board.getCellInBoard(x, y))
            x+=1
            self.removeTileFromPlayer(i)
        elif orientation == "H" or orientation == "h":
            self.board.addTileToCell(x, y, Tile(
                self.current_player.tiles[i].letter,
                self.current_player.tiles[i].value
            ))
            self.score.append(self.board.getCellInBoard(x, y))
            y+=1
            self.removeTileFromPlayer(i)
    
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
                letter = self.isSpecial(letter)
                if (letter == str(self.board.getCellInBoard(x, y)).lower() and letter == self.current_player.tiles[i].letter.lower()):
                    self.scoreMove(orientation)
                    break;
                if letter == str(self.board.getCellInBoard(x, y)).lower():
                    self.scoreMove(orientation)
                    break;
                if (
                    letter == self.current_player.tiles[i].letter.lower()
                    or letter == str(self.board.getCellInBoard(x, y)).lower()
                ):
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