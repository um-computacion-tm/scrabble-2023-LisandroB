import unittest, pathlib

if __name__ == "__main__":
    loader = unittest.TestLoader()
    loader.testMethodPrefix = "test_wrongTurnEndGame"
    suite = loader.discover(str(pathlib.Path.cwd().joinpath("tests")))
    unittest.TextTestRunner(failfast=True).run(suite)