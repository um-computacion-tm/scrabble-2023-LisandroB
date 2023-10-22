# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Modified [22/10/23]
- validateWord function in scrabble.py, now doesn't search in dict as some words don't work well
- location input order in cli.py
### Fixed [22/10/23]
- coordinates order, now corrent (was y, x - now x, y)
### Added [22/10/23]
- test_validateGameHorizontalConExtra in test_scrabble_game.py
### Added [21/10/23]
- isWordInBoard function in scrabble.py
- unidecode in requirements.txt, added as class in player.py and scrabble.py
- test_validateGameHorizontalAndVerticalWithDoubleLetter, test_validateGameHorizontalConEñe, test_validateGameHorizontalConTilde, 
test_validateGameHorizontalAndVerticalWithDoubleLetter in test_scrabble_game.py
### Modified [21/10/23]
- test_word_out_of_board,test_place_word_empty_board_horizontal_wrong, test_place_word_empty_board_vertical_fine, test_boardEmptyPlaceWrongVerticalWord, test_word_out_of_board in test_board.py
- test_place_word_cross_vertical_fine, test_place_word_wrong in test_cli.py
- test_validateGameHorizontalAndVertical in test_scrabble_game.py
- logic in validateWord function in scrabble.py
- logic in validate_word_inside_board function in board.py
- logic for coordinates [line 96, 102, 106] in putWord function in scrabble.py
### Added [20/10/23]
- test_validateGameVertical in test_scrabble_game.py
### Modified [20/10/23]
- addTileToCell function in board.py 
- logic in cli.py, added unused validateTurn function
- putWord function in scrabble.py
### Added [19/10/23]
- __str__ in Tile class in models.py
- test_validateGameVertical, test_validateGameHorizontal, test_validateGameFixed, test_validateGameHuh in test_scrabble_game.py
### Modified [19/10/23]
- logic in validateWord function in scrabble.py
- logic in putWord function in scrabble.py
### Added [18/10/23]
- __str__ in cell.py
### Modified [18/10/23]
- addTileToCell function in board.py
- .coverage.xml 
- .codeclimate.yml
### Added [17/10/23]
- test_validateGameHuh in test_scrabble_game.py
- shuffleTiles function to player.py
- removeTile function in cell.py
- score attribute in player class initialization
- score keeping in each player instance in putWord method
- test_putWordGetScore in test_scrabble_game.py
- getScore function in scrabble.py
- removeTile function in scrabble.py
- test_addTileToCell in test_board.py
- test_reprMultiplier, reprTile, reprNone in test_cell.py
- test_shufflinTiles in test_player.py
- test_getScore, test_validateTurnRight, validateTurnWrong in test_scrabble_game.py
### Fixed [17/10/23]
- line 31 in board.py, changed _.multiplier and _.multiplier_type to == "" instead of == None
- all tests in test_wordvalue.py
### Modified [17/10/23]
- validateTurn function in scrabble.py
- logic order in cli.py
- addTileToCell function in board.py, added logic for avoiding already set tiles on board
### Added [16/10/23]
- fillTiles function in player.py
- tests in test_player.py
### Fixed [16/10/23]
- getTiles function
- Player class init in player.py, parameter bagTiles added
### Modified [16/10/23]
- order in cli.py 
- validateTurn function in scrabble.py
### Added [15/10/23]
- dev branch for updates starting from now, will publish finished project in main branch when done
- tests in test_scrabble_game.py
- initializing player now gets tiles from bag
### Fixed [15/10/23]
- logic for putWord method
- passing player's coordinates input in client as integer instead of string 
### Modified [15/10/23]
- validate_word_inside_board method
- indentation in test_player.py 
### Added [13/10/23]
- removeTiles method
- test in test_scrabble_game.py
### Modified [13/10/23]
- putWord method
### Added [12/10/23]
- putWord, validateTurn methods
- tests in test_scrabble_game.py, test_player.py
### Fixed [11/10/23]
- showBoard method
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