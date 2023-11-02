# ScrabbleUM
Welcome to ScrabbleUM! This a _simple_ Scrabble clone made in Python that is playable through the terminal, it uses a spanish dictionary. Scrabble originally is a turn-based board game where 2 to 4 players score points by placing tiles [each containing a letter and its value] onto a game board composed of a 15x15 grid of squares. Each player has a set of finite tiles that they have to use every turn to form words in the game board, putting the exact coordinates and orientation they want them to be positioned in. 

The game ends when there are no more tiles in the bag or when the users choose to do so, the winner being the player with the most points up to the last turn.

Psst! If your word has an accent [spanish dictionary], it can be put on the board. ;)

## Requirements:
- Git
- Docker
- Python
- Active internet connection

## Installation:
1. Clone the repository
```
    git clone https://github.com/um-computacion-tm/scrabble-2023-LisandroB 
```
2. Enter the directory
```
    cd ./scrabble-2023-LisandroB
```
3. Build Docker image [make sure you copy the dot too!]
```
    docker build -t scrabbleum .
```
4. Run!
```
    docker run -it scrabbleum
```

Have fun!

[![um-computacion-tm](https://circleci.com/gh/um-computacion-tm/scrabble-2023-LisandroB.svg?style=svg)](https://app.circleci.com/pipelines/github/um-computacion-tm/scrabble-2023-LisandroB?branch=main)

<a href="https://codeclimate.com/github/um-computacion-tm/scrabble-2023-LisandroB/maintainability"><img src="https://api.codeclimate.com/v1/badges/5f39fbeaa1318a0b90e2/maintainability" /></a>

<a href="https://codeclimate.com/github/um-computacion-tm/scrabble-2023-LisandroB/test_coverage"><img src="https://api.codeclimate.com/v1/badges/5f39fbeaa1318a0b90e2/test_coverage" /></a>

Author Lisandro Brasolin, 
