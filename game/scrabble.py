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

    def validateTurn(self, word, location, orientation):
        if len(self.bagTiles.tiles) > 0 and len(self.current_player.tiles) > 0:
            return self.putWord(word, location, orientation)
        elif len(self.current_player.tiles) == 0 or len(self.bagTiles.tiles) == 0:
            self.endGame()

    def getScore(self):
        print("------------------------ Scoreboard ------------------------")
        for _ in self.players:
            print(f"Player {_.id}: {_.score}")

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
    
    def checkIfFirstTurn(self, word, location, orientation):
        (x, y) = location
        if self.turn == 1:
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
        elif self.turn > 1: 
            return True;

    def checkIfNextToTile(self, word, location, orientation):
        if not self.isNextToTile(word, location, orientation) == None:
            return True;
        else:
            raise Exception("Palabra debe continuar con las del tablero!")

    def isNextToTile(self, word, location, orientation):
        (x, y) = location
        if self.turn > 1:
            for _ in word:
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
        else:
            return True;

    def validateWord(self, word, location, orientation):
        if (
            self.current_player.hasWord(word)
            and 
            self.board.validate_word_inside_board(word, location, orientation)
            and 
            dict(word)
            and
            self.checkIfFirstTurn(word, location, orientation)
        ):
            return self.checkIfNextToTile(word, location, orientation)
        elif (
            self.isWordInBoard(word, location, orientation)
            and
            self.board.validate_word_inside_board(word, location, orientation)
            and
            dict(word)
            and
            self.checkIfFirstTurn(word, location, orientation)
        ):
            return self.checkIfNextToTile(word, location, orientation)

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

    def putWord(self, word, location, orientation):
        (x, y) = location
        score = []
        if self.validateWord(word, location, orientation):
            word = [char for char in word]
            for letter in word:
                for i in range(len(self.current_player.tiles)): 
                    letter = self.isSpecial(letter)
                    if (letter == str(self.board.getCellInBoard(x, y)).lower() and letter == self.current_player.tiles[i].letter.lower()):
                        if orientation == "V" or orientation == "v":
                            score.append(self.board.getCellInBoard(x, y))
                            x+=1
                        elif orientation == "H" or orientation == "h":
                            score.append(self.board.getCellInBoard(x, y))
                            y+=1
                        break;
                    if letter == str(self.board.getCellInBoard(x, y)).lower():
                        if orientation == "V" or orientation == "v":
                            score.append(self.board.getCellInBoard(x, y))
                            x+=1
                        elif orientation == "H" or orientation == "h":
                            score.append(self.board.getCellInBoard(x, y))
                            y+=1
                        break;
                    if (
                        letter == self.current_player.tiles[i].letter.lower()
                        or letter == str(self.board.getCellInBoard(x, y)).lower()
                    ):
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
            self.current_player.score += self.board.calculateWordValue(score)
            return True