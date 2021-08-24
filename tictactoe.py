import os
from time import sleep
clear = lambda: os.system('cls')

class Player():
    def __init__(self, token):
        self._token = token
        self._wins = 0

    @property
    def token(self):
        return self._token

    @property
    def wins(self):
        return self._wins

    def add_win(self):
        self._wins += 1


class Board():
    def __init__(self):
        self._board = {
            7:' ', 8:' ', 9:' ',
            4:' ', 5:' ', 6:' ',
            1:' ', 2:' ', 3:' '
        }
        self._availables_squares = [n for n in range(1, 10)]

    def reset(self):
        self._board = {
            7:' ', 8:' ', 9:' ',
            4:' ', 5:' ', 6:' ',
            1:' ', 2:' ', 3:' '
        }
        self._availables_squares = [n for n in range(1, 10)]

    def show(self):
        print(f'''
 {self._board[7]} | {self._board[8]} | {self._board[9]}
---+---+---
 {self._board[4]} | {self._board[5]} | {self._board[6]}
---+---+---
 {self._board[1]} | {self._board[2]} | {self._board[3]}
''')

    def is_full(self):
        full = True
        for v in self._board.values():
            if v == ' ':
                full = False
        return full


    def mark(self, square, player):
        if square in self._availables_squares:
            self._board[square] = player
            self._availables_squares.remove(square)

    def check_win(self, player):
        # Check Horizontal Win
        if self._board[7] == player and self._board[8] == player and self._board[9] == player:
            return True
        if self._board[4] == player and self._board[5] == player and self._board[6] == player:
            return True
        if self._board[1] == player and self._board[2] == player and self._board[3] == player:
            return True

        #Check Vertical Win
        if self._board[7] == player and self._board[4] == player and self._board[1] == player:
            return True
        if self._board[8] == player and self._board[5] == player and self._board[2] == player:
            return True
        if self._board[9] == player and self._board[6] == player and self._board[3] == player:
            return True

        #Check Diagonal Wins
        if self._board[7] == player and self._board[5] == player and self._board[3] == player:
            return True
        if self._board[1] == player and self._board[5] == player and self._board[9] == player:
            return True


class Game():
    def __init__(self, player1='X', player2='O'):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.player_turn = self.player1
        self.board = Board()
        self.draws = 0

    def check_draw(self):
        if self.board.is_full() == True:
            return True

    def change_turn(self):
        if self.player_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1


    def move(self, prompt):
        x = input(prompt)
        while x.isnumeric() == False:
            if x.isnumeric():
                break
            else:
                print('Digite um número.')
                x = input(prompt)
        return x

    def show_scoreboard(self):
        print('-'*30)
        print(f'PLAYER {self.player1.token} | WINS: {self.player1.wins} |')
        print(f'PLAYER {self.player2.token} | WINS: {self.player2.wins} |')
        print('-'*30)
        print(f'PLAYER {self.player_turn.token} TURN')

    def play(self):
        while True:
            clear()
            self.show_scoreboard()
            self.board.show()
            while True:
                move = int(self.move('Sua jogada [1-9]: '))
                if move in self.board._availables_squares:
                    self.board.mark(move, self.player_turn.token)
                    if self.board.check_win(self.player_turn.token):
                        clear()
                        print(f'PLAYER {self.player_turn.token} WINS THE ROUND!')
                        self.board.show()
                        self.board.reset()
                        sleep(5)
                        if self.player_turn == self.player1:
                            self.player1.add_win()
                        else:
                            self.player2.add_win()
                        self.change_turn()
                        break
                    if self.check_draw():
                        clear()
                        print('DRAW')
                        self.board.show()
                        self.board.reset()
                        sleep(5)
                        break
                    self.change_turn()
                    break


TICTACTOE = Game()
TICTACTOE.play()