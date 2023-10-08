import random
from game.language.letters_spa import Letters
class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class BagTiles:
    def __init__(self):
        self.tiles = []

    def initBagTiles(self):
        def create(dict, n):
            for key, value in dict.items():
                for _ in range(0, value):
                    self.tiles.append(Tile(key, n))
        unpacking = [(Letters.onePoint, 1),
            (Letters.twoPoints, 2),
            (Letters.threePoints, 3),
            (Letters.fourPoints, 4),
            (Letters.fivePoints, 5),
            (Letters.eightPoints, 8),
            (Letters.tenPoints, 10)] 
        for z in unpacking:
            create(*z)
        return self.tiles;
    
    def getTiles(self):
        bag = self.initBagTiles()
        random.shuffle(bag)
        for _ in range(0, 91):
            self.tiles.pop()
        return self.tiles
          
    def take(self, count):
        self.getTiles()
        for _ in range(count):
            self.tiles.pop()
        return self.tiles

    def put(self, tiles):
        self.tiles.extend(tiles)