Commands = ("Your available commands are: \n"
            "1. game.make_move(pos1, pos2): where pos1 is your column position, and pos2 is your row position,"
            " with (0,0) being top left and (2,2) being bottom right \n"
            "2. game.print_board() to see the current board \n"
            "3. game.get_player_turn() to see whose turn it is \n")

class TicTacToe:
    """
    Represents the game of tic tac toe.
    """

    def __init__(self):
        """
        Initializes the game settings
        """
        self._player_1 = "X"
        self._player_2 = "O"
        self._current_turn = "X"
        self._turns_remaining = 9
        self._game_state = "ONGOING"
        self._game_board = []
        self.initialize_board()

    def initialize_board(self):
        """
        Initializes the game board
        """
        for i in range(3):
            self._game_board.append(["_", "_", "_"])

    def print_board(self):
        """
        Prints out the current game board
        """
        for rows in self._game_board:
            print(" ".join(rows))

    def change_turns(self):
        """
        Changes the player turn to the other player
        """
        if self.get_player_turn() == "X":
            self.set_player_turn("O")
            self._turns_remaining -= 1
        else:
            self.set_player_turn("X")
            self._turns_remaining -= 1

    def set_player_turn(self, player_turn):
        """
        Sets the player turn to the entered parameter
        """
        self._current_turn = player_turn
        return self._current_turn

    def get_player_turn(self):
        """
        Returns the current players turn
        """
        return self._current_turn

    def get_turns_remaining(self):
        """
        Returns the number of turns left
        """
        return self._turns_remaining

    def set_game_state(self, game_state):
        """
        Sets the game state
        """
        self._game_state = str(game_state.upper())
        return self._game_state

    def get_game_state(self):
        """
        Get the game state
        """
        return self._game_state

    def get_commands(self):
        """
        Displays the methods available for player use
        """
        print(Commands)

    def check_for_win(self):
        """
        Checks if there are any winnings moves
        """

        # checks for vertical wins
        if self._game_board[0][0] == "X" and self._game_board[0][1] == "X" and self._game_board[0][2] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[0][0] == "O" and self._game_board[0][1] == "O" and self._game_board[0][2] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")
        elif self._game_board[0][1] == "X" and self._game_board[1][1] == "X" and self._game_board[2][1] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[0][1] == "O" and self._game_board[1][1] == "O" and self._game_board[2][1] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")
        elif self._game_board[0][2] == "X" and self._game_board[1][2] == "X" and self._game_board[2][2] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[0][2] == "O" and self._game_board[1][2] == "O" and self._game_board[2][2] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")

        # checks for horizontal wins
        elif self._game_board[0][0] == "X" and self._game_board[0][1] == "X" and self._game_board[0][2] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[0][0] == "O" and self._game_board[0][1] == "O" and self._game_board[0][2] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")
        elif self._game_board[1][0] == "X" and self._game_board[1][1] == "X" and self._game_board[1][2] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[1][0] == "O" and self._game_board[1][1] == "O" and self._game_board[1][2] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")
        elif self._game_board[2][0] == "X" and self._game_board[2][1] == "X" and self._game_board[2][2] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[2][0] == "O" and self._game_board[2][1] == "O" and self._game_board[2][2] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")

        # check for diagonal wins
        elif self._game_board[0][0] == "X" and self._game_board[1][1] == "X" and self._game_board[2][2] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[0][0] == "O" and self._game_board[1][1] == "O" and self._game_board[2][2] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")
        elif self._game_board[0][2] == "X" and self._game_board[1][1] == "X" and self._game_board[2][0] == "X":
            print("X has won")
            self.set_game_state("X HAS WON")
        elif self._game_board[0][2] == "X" and self._game_board[1][1] == "X" and self._game_board[2][0] == "O":
            print("O has won")
            self.set_game_state("O HAS WON")

    def make_move(self, pos1, pos2):
        """
        Makes a move using board positions, sets the piece depending on player turn
        """

        if self._game_state != "ONGOING":
            print("Game is over, no more moves available")
            return

        if pos1 > 2 or pos1 < 0:
            return "Not a valid position"
        elif pos2 > 2 or pos1 < 0:
            return "Not a valid position"

        if self._game_board[pos1][pos2] != "_":
            return "Space is already occupied"

        if self._current_turn == "X":
            self._game_board[pos1][pos2] = "X"
        elif self._current_turn == "O":
            self._game_board[pos1][pos2] = "O"

        self.check_for_win()
        self.change_turns()

        if self.get_turns_remaining() == 0:
            self.set_game_state("TIED")
            print(self._game_state)


game = TicTacToe()
game.get_commands()

# ----------- Play using the game commands under this line ----------









# ----------- Play using the game commands above this line ----------

game.print_board()
