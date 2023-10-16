from game.scrabble import ScrabbleGame
from game.board import Board

class Game():
    def cli(self):
        board = Board()
        print("Bienvenido a ScrabbleUM!")
        while True:
            try: 
                players_count = int(input("Ingrese cantidad de jugadores: "))
                if players_count <= 1 or players_count > 4:
                    raise ValueError
                break
            except ValueError:
                print("Valor invalido")
        scrabbleGame = ScrabbleGame(players_count)
        print("Cantidad de jugadores: ", len(scrabbleGame.players))
        while scrabbleGame.validateTurn:
            scrabbleGame.next_turn()
            print(f"Turno del jugador {scrabbleGame.current_player.id}")
            print(scrabbleGame.current_player.tiles)
            word = input("Ingrese palabra: ")
            x = input("Ingrese posicion X: ")
            y = input("Ingrese posicion Y: ")
            location = (int(x), int(y))
            orientation = input("Ingrese orientacion (V/H): ")
            scrabbleGame.putWord(word, location, orientation)
            # refill tiles of current_player from bagtiles
            self.showBoard(scrabbleGame.board)
        else:
            print("Juego terminado! Desea jugar otra vez? (Y/N): ")
        
    def showBoard(self, board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(1, 16)]))
        for row_index, row in enumerate(board.grid):
            print(str(row_index+1).rjust(2) + '| ' + ' '.join([repr(cell) for cell in row]))