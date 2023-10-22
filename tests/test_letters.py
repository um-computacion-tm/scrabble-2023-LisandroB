import unittest;
from game.language.letters_spa import Letters as LettersSpa;

class TestLetters(unittest.TestCase):
    def test_spaletinit(self):
        self.assertEqual(all([LettersSpa.eightPoints,
            LettersSpa.fivePoints,
            LettersSpa.fourPoints,
            LettersSpa.onePoint,
            LettersSpa.tenPoints,
            LettersSpa.threePoints]), True)

if __name__ == '__main__':
    unittest.main()