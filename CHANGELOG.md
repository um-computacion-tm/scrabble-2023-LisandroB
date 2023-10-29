# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added [29/10/23]
- checks for special characters in hasWord function in player.py
- checkIfNextToTile, isSpecial functions [reformatted prev code that worked, made into separate functions]
- test_validateWordWithTildeAndÑ, test_validateWordMuchasTildes, test_validateWordNotFoundInDictionary in test_scrabble_game.py
### Modified [29/10/23]
- validateWord function in scrabble.py now uses checkIfNextToTile
- putWord function in scrabble.py now uses isSpecial
- cli.py, changed how the score is printed to avoid a stray None result and when player is asked for a word, now specifies that it needs a lowercase word
- dictionary.py, now it throws an error when word is not found in dict
- test_invalid in test_dictionary.py now asserts exception
### Added [28/10/23]
- self.turn attribute, checkIfFirstTurn and isNextToTile functions
- test_firstTurnThenEnterWord in test_cli.py
- test_putWordThroughCenter, test_putWordThroughCenterWrong, test_validateGameHorizontalConExtraDoble in test_scrabble_game.py
### Modified [28/10/23]
- next_turn, validateWord, putWord functions in scrabble.py
- game logic for cli function in cli.py
- tests in test_player.py
### Added [26/10/23]
- addMultipleTilesToCellAddScoreRemoveTile, addScoreThenMoveOneTile, moveOneTile, checkIfWordAlreadyThere, removeTileFromPlayer, checkIfNonUnicode functions in scrabble.py
- checkIfWordInBoard function in board.py
- test_wrongTileToCell in test_board.py
- test_firstTurnThenEnterWord in test_cli.py
- test_validateGameHorizontalConExtra in test_scrabble_game.py
### Modified [26/10/23]
- logic in addTileToCell, validate_word_inside_board functions in board.py
- logic in validateWord function in scrabble.py
### Added [25/10/23]
- swapTiles function in player.py
- test_wrongStart, test_initStartPlayerCount, test_firstTurnWordNotFound, test_firstTurnShuffle, test_firstTurnThenPass, test_firstTurnThenExit, test_firstTurnThenWrongInput, test_firstTurnThenSecondChoice in test_cli.py
- test_playerHasSwappedAllTiles, test_playerHasSwappedSomeTiles, test_playerHasSwappedOneTile in test_player.py
### Modified [25/10/23]
- logic in cli.py, now second choice works as expected [swapTiles]
- fourth choice in cli.py, now sleeps for one and a half seconds
- fillTiles in player.py, now shuffles tiles before filling
### Added [23/10/23]
- exceptions to validate_word_inside_board, addTileToCell functions in board.py
- exception to isWordInBoard, validateWord, putWord functions in scrabble.py
- conditional loop to cli.py, now menu doesn't always go to next turn when choosing
### Modified [23/10/23]
- isWordInBoard function in scrabble.py
- game loop in cli.py
- validate_word function in dictionary.py
- hasWord function in player.py
- tests test_word_out_of_board, test_place_word_empty_board_horizontal_wrong, test_boardEmptyPlaceWrongVerticalWord in test_board.py
- test_place_word_wrong in test_cli.py
- test_connection_error in test_dictionary.py
- test_playerAlmostHasWord in test_player.py
- test_validateWordFalse, test_validateTurnWrong, test_validateTurnRight, test_putWordFalse, test_putWordFalseAgain, test_validateGameHorizontalConExtra in test_scrabble_game.py
### Added [22/10/23]
- test_validateGameHorizontalConExtra in test_scrabble_game.py
### Modified [22/10/23]
- validateWord function in scrabble.py, now doesn't search in dict as some words don't work well
- location input order in cli.py
- choice 5 [exit game] in cli.py
- getScore function in scrabble.py now doesn't return true when called
- tests in test_scrabble_game.py
- .coveragerc 
### Fixed [22/10/23]
- coordinates order, now correct (was y, x // now x, y)
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
### Modified [16/10/23]
- order in cli.py 
- validateTurn function in scrabble.py
### Fixed [16/10/23]
- getTiles function
- Player class init in player.py, parameter bagTiles added
### Added [15/10/23]
- dev branch for updates starting from now, will publish finished project in main branch when done
- tests in test_scrabble_game.py
- initializing player now gets tiles from bag
### Modified [15/10/23]
- validate_word_inside_board method
- indentation in test_player.py 
### Fixed [15/10/23]
- logic for putWord method
- passing player's coordinates input in client as integer instead of string 
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
- tests that calculate the value of each letter/word
- GitHub Webhooks for CodeClimate
- env from Windows. [virtual environment]
- CodeClimate's Test Reporter ID to CircleCI's environmental variable 