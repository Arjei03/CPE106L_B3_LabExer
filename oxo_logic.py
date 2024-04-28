''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()
'''

import os, random
import oxo_data

class Game():
    def newGame():
        ' return new empty game'
        return list(" " * 9)

    def saveGame(game):
        ' save game to disk '
        oxo_data.saveGame(game)
        
    def restoreGame():
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                return game
            else: return list()
        except IOError:
            return list()
        
    def _generateMove(game):
        ''' generate a random cell from thiose available.
            If all cells are used return -1'''
        options = [i for i in range(len(game)) if  game[i] == " "]
        if options:
            return random.choice(options)
        else: return -1
        
    def _isWinningMove(game):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a,b,c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def userMove(game, cell):
        if game[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            game[cell] = 'X'
        if Game._isWinningMove(game):
            return 'X'
        else:
            return ""

    def computerMove(game):
        cell = Game._generateMove(game)
        if cell == -1:
            return 'D'
        game[cell] = 'O'
        if Game._isWinningMove(game):
            return 'O'
        else:
            return ""

def test():
    result = ""
    game = Game.newGame()  # Initialize a new game using newGame() method
    while not result:
        print(game)
        try:
           result = Game.userMove(game, Game._generateMove(game))  # Call userMove() with game instance and generated move
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = Game.computerMove(game)  # Call computerMove() with game instance
            
        if not result: continue
        elif result == 'D':
            print("It's a draw")
        else:
            print("Winner is:", result)
        print(game)

if __name__ == "__main__":
    test()
