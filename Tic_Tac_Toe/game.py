class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #We will use a singlelist to rep 3x3 board
        self.current_winner = None # Keep track of winner!\

    def print_board(self):
        #This is just getting the rows
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print(" | " + " | ".join(row) + " | ")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(" | " + " | ".join(row) + " | ")

    def available_moves(self):
        return [i for i, pot in enumerate(self.board) is spot == " "]
    # moves = []
    #for (i, spot) in enumerate(self.board):
    #   #["x", "x", "o"] --> [(0, 'X'), (1, 'X'), (2, 'o')]
    #   if spot == " ":
    #       moves.append(i)
    #return moves

    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #Starting letter
    #iterate while the game still has empty squares
    # (we dont have to worry abput winner because we'll just return that
    # # which breaks the loop)

    while game.empty_squares():
        pass