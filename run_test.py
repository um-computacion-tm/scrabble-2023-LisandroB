import unittest, pathlib

if __name__ == "__main__":
    loader = unittest.TestLoader()
    loader.testMethodPrefix = "test"
    suite = loader.discover('/home/rdnsl/Downloads/vvv/game')
    unittest.TextTestRunner(failfast=True).run(suite)