import unittest
from game.cell import Cell
from game.models import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(cell.multiplier,2,)
        self.assertEqual(cell.multiplier_type,'letter')
        self.assertIsNone(cell.tile)
        self.assertEqual(cell.calculate_value(), 0)

    def test_reprMultiplier(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(repr(cell), "Lx2")

    def test_reprTile(self):
        cell = Cell(multiplier=2, multiplier_type='letter', tile=Tile(letter="L", value=3))
        self.assertEqual(repr(cell), "L:3")
    
    def test_reprNone(self):
        cell = Cell(multiplier=1, multiplier_type='')
        self.assertEqual(repr(cell), "   ")

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        add = Tile('P', 3)
        cell.addTile(add)
        self.assertEqual(cell.tile, add)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        add = Tile('P', 3)
        cell.addTile(add)
        self.assertEqual(cell.calculate_value(), 6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        cell.addTile(Tile('P', 3))
        self.assertEqual(cell.calculate_value(), 3)

if __name__ == '__main__':
    unittest.main()
