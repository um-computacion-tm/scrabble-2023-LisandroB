import unittest;
from game.letters import Letters;

class TestLetters(unittest.TestCase):
    def test_engletinit(self):
        self.assertEqual(all([Letters.eightPoints,
            Letters.fivePoints,
            Letters.fourPoints,
            Letters.onePoint,
            Letters.tenPoints,
            Letters.threePoints]), True)
        
if __name__ == '__main__':
    unittest.main()