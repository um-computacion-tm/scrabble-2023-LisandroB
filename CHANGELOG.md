# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Fixed [11/10/23]
- showBoard
- function names [addTileToCell, getCellInBoard] in board.py
- tests in test_player.py, test_scrabble_game
- multiplier distribution in board
- letter distribution in letters_spa [no longer has 'ch', 'rr' or 'll' tiles]
### Added [11/10/23]
- tests in test_scrabble_game.py, test_models.py, test_cli.py
- logic in hasWord (player.py)
- moved showBoard to cli.py
### Fixed [10/10/23]
- tests for test_scrabble_game.py, test_models.py
- player/bagtile logic
### Added [10/10/23]
- tests in test_player.py
### Added [09/10/23]
- files play.py, run_test.py, dictionary.py, test_dictionary.py, 
- functions addTileToCell, getCellInBoard, applyMultipliersToList, fillWithMultipliers, applyMultipliersToCoords, checkIfEmpty, showBoard
- tests in test_board
### Added [07/10/23]
- tests, multipliers
- new file for english letters
### Added [06/10/23]
- tests for test_board.py
### Fixed [06/10/23]
- test_board.py non-functional tests
### Added [05/10/23]0
- functions (addTile, isEmpty, addValue)
- tests for test_board.py
### Added [04/10/23] 
- more tests for scrabble_game
- word validation, parsing and putting [logic missing, init idea]
- cli.py, test_cli.py
- tests for test_board
- board functionality [validate word inside board, is empty]
### Added [03/10/23]
- tests for letters.py
- tests for test_player.py, logic for letter checking in player.py
### Fixed [03/10/23]
- general code indentation structure from tests/game, made it more my like my own code
### Fixed [02/10/23]
- tests + logic for score
### Fixed [30/09/23]
- take/put functions
- player functionality
### Fixed [29/09/23]
- language for tile distribution [letter distribution was following english scrabble's rules, now changed to spanish]
### Added [27/09/23]
- shuffling tiles before being inserted in bag
- better tilebag init code
- badges [CodeClimate, CircleCI]
### Added [30/08/23]
- tests that calculates the value of each letter/word
- GitHub Webhooks for CodeClimate
- env from Windows. [virtual environment]
- CodeClimate's Test Reporter ID to CircleCI's environmental variable 