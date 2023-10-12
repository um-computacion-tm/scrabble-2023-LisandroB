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
        scrabble_game = ScrabbleGame(players_count)
        print("Cantidad de jugadores: ", len(scrabble_game.players))
        while scrabble_game.validateTurn:
            scrabble_game.next_turn()
            print(f"Turno del jugador {scrabble_game.current_player.id}")
            word = input("Ingrese palabra: ")
            location_x = input("Ingrese posicion X: ")
            location_y = input("Ingrese posicion Y: ")
            location = (location_x, location_y)
            orientation = input("Ingrese orientacion (V/H): ")
            scrabble_game.validateTurn(word, location, orientation)
            # refill tiles of current_player from bagtiles
            self.showBoard(board)
        else:
            print("Juego terminado! Desea jugar otra vez? (Y/N): ")
        
    def showBoard(self, board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(1, 16)]))
        for row_index, row in enumerate(board.grid):
            print(str(row_index+1).rjust(2) + '| ' + ' '.join([repr(cell) for cell in row]))