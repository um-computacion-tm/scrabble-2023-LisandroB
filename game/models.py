import random
from game.letters import Letters
class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class BagTiles:
    def __init__(self):
        self.tiles = []

    def initBagTiles(self, dict, n):
        unpacking = [Tile(Letters.onePoint, 1),
                Tile(Letters.twoPoints, 2),
                Tile(Letters.threePoints, 3),
                Tile(Letters.fourPoints, 4),
                Tile(Letters.fivePoints, 5),
                Tile(Letters.eightPoints, 8),
                Tile(Letters.tenPoints, 10)]    
        for key, value in dict.items():
            for _ in range(0, value):
                self.tiles.append([Tile(key, n)])
        for z in unpacking:
            self.initBagTiles(*z)
    def take(self, count):
        None
        # bag
        # for _ in range(count):
        #   tiles.append(self.tiles.pop())
        # return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
