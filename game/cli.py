from game.scrabble import ScrabbleGame
from game.board import Board
import time as time

class Game():
    def getPlayers(self, input):
        while True:
            try: 
                playerCount = int(input("Ingrese cantidad de jugadores [2-4]: "))
                if playerCount <= 1 or playerCount > 4:
                    raise ValueError
                else:
                    return playerCount
            except ValueError:
                print("Valor invalido")

    def printTiles(self, game):
        lst = []
        for _ in game.current_player.tiles:
            lst.append(f"{_.letter}:{_.value}")
        txt = ', '.join(lst)
        print(txt.center(65))

    def getMenu(self, game):
        print(f" ")
        txt = f"Turno {game.turn} - Jugador {game.current_player.id}"
        print(txt.center(65))
        self.showBoard(game.board)
        print(f" ")
        txt2 = f"Fichas restantes: {len(game.bagTiles.tiles)}"
        print(txt2.center(65))
        print(f" ")
        self.printTiles(game)
        print("------------------------------------------------".center(65))
        print("1. Poner palabra".center(65))
        print("2. Cambiar tiles".center(65))
        print("3. Shuffle!".center(65))
        print("4. Pasar turno".center(65))
        print("5. Mostrar puntaje".center(65))
        print("6. Terminar juego".center(65))
        print("------------------------------------------------".center(65))
    
    def playWord(self, game):
        word = input("Ingrese palabra en minúscula: ")
        x = input("Ingrese posicion X: ")
        y = input("Ingrese posicion Y: ")
        location = (int(y), int(x))
        orientation = input("Ingrese orientacion (V/H): ")
        game.putWord(word, location, orientation)
        game.current_player.fillTiles(game.bagTiles)
    
    def changeTiles(self, game):
        list = input("Elija qué tiles cambiar! Separe con coma, por ej: 1, 5, 3: ")
        res = [eval(i) for i in list.split(', ')]
        game.current_player.swapTiles(game.bagTiles, res)
        print(game.current_player.tiles)
        print("Tiles cambiadas!")
    
    def shufflePlayersTiles(self, game):
        game.current_player.shuffleTiles()
        self.printTiles(game)
        print("Shuffled!".center(65))
    
    def passTurn(self, game):
        if game.turn > 1:
            print("Pasaste tu turno!")
            time.sleep(1.5)
        else:
            raise Exception("No podés pasar el primer turno!")
    
    def quit(self, game):
        exit = input("Está seguro de terminar la partida? Y/N: ")
        if exit == "Y" or exit == "y":
            game.endGame()
            time.sleep(1.5)
        if exit == "N" or exit == "n":
            raise Exception("Volviendo a tu turno!")
        
    def mainMenu(self, game):
        while True:    
            try:
                self.getMenu(game)
                choice = input("Qué desea hacer?: " )
                if choice == "1":
                    self.playWord(game)
                    break;
                elif choice == "2":
                    self.changeTiles(game)
                    time.sleep(1.5)
                elif choice == "3":
                    self.shufflePlayersTiles(game)
                    time.sleep(1.5)
                elif choice == "4":
                    self.passTurn(game)
                    break;
                elif choice == "5":
                    game.getScore()
                    time.sleep(2)
                elif choice == "6":
                    self.quit(game)
                    raise AssertionError
                else:
                    raise Exception("Valor equivocado, inténtelo otra vez") 
            except AssertionError:
                global breaker
                breaker = True;
                return False;
            except Exception as err:
                print(err.args[0])
                time.sleep(1.5)

    def cli(self):
        global breaker
        breaker = False
        print("Bienvenido a ScrabbleUM!")
        scrabbleGame = ScrabbleGame(self.getPlayers(input))
        while scrabbleGame.validateTurn():
            try:
                scrabbleGame.next_turn()
                self.mainMenu(scrabbleGame)
            except False:
                print("Valor equivocado!")
            if breaker == True:
                break;

    def showBoard(self, board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(1, 16)]))
        for row_index, row in enumerate(board.grid):
            print(str(row_index+1).rjust(2) + '| ' + ' '.join([repr(cell) for cell in row]))