from game.scrabble import ScrabbleGame
from game.board import Board

class Game():
    def cli(self):
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
        while scrabbleGame.validateTurn:
            try:
                scrabbleGame.next_turn()
                print(f"{scrabbleGame.getScore()}")
                print(f"Turno del jugador {scrabbleGame.current_player.id}")
                self.showBoard(scrabbleGame.board)
                print(scrabbleGame.current_player.tiles)
                print("------------------------------------------------")
                print("1. Poner palabra")
                print("2. Cambiar tiles")
                print("3. Shuffle!")
                print("4. Pasar turno")
                print("------------------------------------------------")
                choice = input("Qué desea hacer?: " )
                if choice == "1":
                    word = input("Ingrese palabra: ")
                    x = input("Ingrese posicion X: ")
                    y = input("Ingrese posicion Y: ")
                    location = (int(y), int(x))
                    orientation = input("Ingrese orientacion (V/H): ")
                    scrabbleGame.validateTurn(word, location, orientation)
                    # calculate and show score
                    scrabbleGame.current_player.fillTiles(scrabbleGame.bagTiles)
                    print("------------------------------------------------")
                elif choice == "2":
                    print("El formato para elegir es del 1 al 7, pudiendo elegir un rango de ellas o una sola")
                    tiles = input("Elija qué tiles cambiar!")
                elif choice == "3":
                    scrabbleGame.current_player.shuffleTiles()
                    print(scrabbleGame.current_player.tiles)
                    print("Shuffled!")
                elif choice == "4":
                    pass;
                else:
                    print("Valor equivocado!")
            except False:
                print("Valor equivocado!")
        else:
            print("Juego terminado! Desea jugar otra vez? (Y/N): ")
        
    def showBoard(self, board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(1, 16)]))
        for row_index, row in enumerate(board.grid):
            print(str(row_index+1).rjust(2) + '| ' + ' '.join([repr(cell) for cell in row]))