from game.board import Board
from game.player import Player
from game.models import BagTiles
class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bagTiles = BagTiles()
        self.players:list[Player] = []
        for index in range(players_count):
            self.players.append(Player())
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]: #Accediendo al ultimo valor de la lista
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def validate_word(self, word, location, orientation):
        '''
        1- Validar que usuario tiene esas letras
        2- Validar que la palabra entra en el tablero
        '''
        self.board.validate_word_inside_board(word, location, orientation)
    
    def get_words():
            '''
            Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
            Preguntar al usuario, por cada una de esas palabras, las que considera reales
            '''
    
    def put_words():
        '''Modifica el estado del tablero con las palabras consideradas como correctas'''
    def calculate_word_value(word):
        result = 0;
        mulres = 1; ## creating a variable for adding whatever the _.multiplier throws back 
        for _ in word:
            if _.multiplier_type=="letter":
                result += _.letter.value * _.multiplier
            elif _.multiplier == None or _.multiplier_type == None:
                result += _.letter.value 
            elif _.multiplier_type=="word":
                mulres = _.multiplier
                result += _.letter.value
        return mulres * result ## multiplying the result when the score is already added