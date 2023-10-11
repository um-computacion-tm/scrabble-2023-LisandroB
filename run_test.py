import unittest, pathlib

if __name__ == "__main__":
    loader = unittest.TestLoader()
    loader.testMethodPrefix = "test_place_word_cross_vertical_fine"
    suite = loader.discover(str(pathlib.Path.cwd().joinpath("tests")))
    unittest.TextTestRunner(failfast=True).run(suite)