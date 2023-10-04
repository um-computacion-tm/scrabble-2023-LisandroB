from game.scrabble import ScrabbleGame

def cli():
    print("Bienvenido a ScrabbleUM!")
    while True:
        try: 
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")
    scrabble_game = ScrabbleGame(players_count=players_count)
    print("Cantidad de jugadores: ", len(scrabble_game.players))
    """ 
    while scrabble_game.validate_turn:
        scrabble_game.next_turn()
        print(f"Turno del jugador {scrabble_game.current_player.id}")
        word = input("Ingrese palabra: ")
        location_x = input("Ingrese posicion X: ")
        location_y = input("Ingrese posicion Y: ")
        location = (location_x, location_y)
        orientation = input("Ingrese orientacion (V/H): ")
        scrabble_game.validate_word(word, location, orientation)
    else:
        print("Juego terminado! Desea jugar otra vez? (Y/N): ")
    """

