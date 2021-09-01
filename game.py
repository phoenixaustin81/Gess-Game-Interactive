import pygame
from board import Board
from piece import Piece
from stone import Stone
from constants import *


class GessGame:
    """
    The GessGame class is used to make and play a game of Gess - a Chess/Go variant board game.
    The game board is stored in a Board object, and managed by the Board class.
    Game pieces are stored in Piece objects, and manipulated by the Piece, Board, and GessGame classes.
    GessGame methods for move validation and execution communicate with the Board and Piece classes.
    GessGame methods for checking the game state or resigning the game do not require communication with other classes.
    """

    def __init__(self, win):
        """
        Initializes the data members of a GessGame object.
        board - stored in a Board object.
        game_state - who, if anyone, won the game
        whose_turn - player whose turn it is to make a move
        up_next - player who is not currently authorized to make a move
        direction - direction of the move being made (list of two integers)
        distance - distance of the move being made
        """
        self._board = Board()
        self._win = win
        self._game_state = "UNFINISHED"
        self._whose_turn = "B"
        self._up_next = "W"
        self._selected = None
        self._direction = None
        self._distance = None

    def update(self):
        """
        Displays the board in its current state to the user.
        """
        self._win.fill(BEIGE)  # fill board with background color
        self.render_font()
        if self._selected:  # fill selected piece with background color
            self._win.fill(TAN,
                           (self._selected[1] * SQUARE_SIZE - SQUARE_SIZE, self._selected[0] * SQUARE_SIZE - SQUARE_SIZE, SQUARE_SIZE * 3, SQUARE_SIZE * 3))
        for row in range(20):
            for col in range(20):
                pygame.draw.rect(self._win,
                                 BLACK,
                                 (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                                 1)
                if self._board.get_game_board()[row + 1][col + 1] == 'W' or self._board.get_game_board()[row + 1][col + 1] == 'B':
                    stone = Stone(row, col, self._board.get_game_board()[row + 1][col + 1])
                    stone.draw(self._win)

        pygame.display.update()

    def render_font(self):
        """
        Determines the proper text string to render and then renders the proper text string.
        """
        if self._game_state == "UNFINISHED":
            if self._whose_turn == "B":
                text = "Black's Turn"
            else:
                text = "White's Turn"

        elif self._game_state == "BLACK_WON":
            text = "Black Won!"

        else:
            text = "White Won!"

        self._win.fill(TEST,
                       (0, 20 * SQUARE_SIZE, SQUARE_SIZE * 20, 100))
        pygame.font.init()
        font = pygame.font.Font("font/ARCADE.TTF", 72)
        img = font.render(text, True, BLACK)
        self._win.blit(img, (5.25 * SQUARE_SIZE, 20.5 * SQUARE_SIZE))

    def select(self, row, col):
        """
        When a piece is selected, its center position is saved for later use as "start" in make_move().
        On the second click, the piece is moved if the move is valid. Otherwise, the piece is deselected.
        """
        piece = Piece((row+1, col+1), self._board.get_game_board())
        if not self._selected:
            if piece.is_empty():
                return
            else:
                self._selected = row, col
        else:
            self.make_move(self._selected, (row, col))
            self._selected = None

    def get_board(self):
        """
        :return: the Board object associated with an instance of GessGame object
        """
        return self._board

    def get_game_state(self):
        """
        :return: a string indicating which player has won, or that the game is unfinished
        """
        return self._game_state

    def resign_game(self):
        """
        Allows a player to concede their demise.
        Changes the game_state attribute depending on whose turn it is,
        which is determined from the whose_turn attribute.
        """
        if self._whose_turn == "B":
            self._game_state = "WHITE_WON"
        else:
            self._game_state = "BLACK_WON"

    def make_move(self, start, end):
        """
        Makes a move if the move is legal and the game is not unfinished.
        A move is legal if the center of the piece starts and finishes on the board, the piece has no stones of the
        opponent, and the direction and distance are valid.
        Validity of direction of movement is determined by checking the orientation of the footprint of a Piece object.
        Validity of distance is determined by whether the piece has a center stone and the attempted distance.
        A move cannot break the mover's own last ring.
        :param start: the starting coordinate of the piece to be moved (list of two integers)
        :param end: the ending coordinate of the piece to be moved (list of two integers)
        :return: True if valid move-request; False if invalid move-request
        """
        start = [start[0]+1, start[1]+1]
        end = [end[0]+1, end[1]+1]

        # if the game is over
        if self._game_state != "UNFINISHED":
            return False

        # if the move is not on the board
        if start[0] > 19 or start[0] < 1 or start[1] > 20 or start[1] < 1:
            return False
        if end[0] > 19 or end[0] < 1 or end[1] > 20 or end[1] < 1:
            return False

        # if the piece has stones of the opponent
        check_piece = Piece(start, self._board.get_game_board())
        if not check_piece.valid_piece(self._up_next):
            return False

        # if the direction and distance are valid, attempt the move
        if self.valid_direction(start, end) and self.valid_distance(start, end):
            return self.board_step(start, end)
        else:
            return False

    def valid_direction(self, start, end):
        """
        Checks whether the direction of a requested move is valid.
        This is determined by checking the orientation of the footprint of a Piece object.
        If direction is valid, the direction attribute is set accordingly.
        Example: an attempted northeastern move would set the direction attribute to [-1, 1].
        :param start: the starting coordinate of the piece to be moved (list of two integers)
        :param end: the ending coordinate of the piece to be moved (list of two integers)
        :return: True if direction of requested move is valid; False if direction of requested move is invalid
        """
        # make a piece object
        moving_piece = Piece(start, self._board.get_game_board())

        # is the piece moving southward?
        if end[0] > start[0]:

            # is the piece moving southeast?
            if end[1] > start[1]:

                # is the move truly diagonal?
                if abs(end[0] - start[0]) == abs(end[1] - start[1]):

                    # is there a stone in the SE position of the piece?
                    if moving_piece.get_piece_SE() == self._whose_turn:
                        self._direction = [1, 1]  # set the direction of the move
                        return True

            # repeat of the above for a southwest move
            elif end[1] < start[1]:
                if abs(end[0] - start[0]) == abs(end[1] - start[1]):
                    if moving_piece.get_piece_SW() == self._whose_turn:
                        self._direction = [1, -1]  # set the direction of the move
                        return True

            # must be direct south movement if reaches this line
            else:
                if moving_piece.get_piece_S() == self._whose_turn:
                    self._direction = [1, 0]  # set the direction of the move
                    return True

        # is the piece moving northward?
        elif end[0] < start[0]:

            # is the piece moving northeast?
            if end[1] > start[1]:

                # is the move truly diagonal?
                if abs(end[0] - start[0]) == abs(end[1] - start[1]):

                    # is there a stone in the NE position of the piece?
                    if moving_piece.get_piece_NE() == self._whose_turn:
                        self._direction = [-1, 1]  # set the direction of the move
                        return True

            # repeat of the above for a northwest move
            elif end[1] < start[1]:
                if abs(end[0] - start[0]) == abs(end[1] - start[1]):
                    if moving_piece.get_piece_NW() == self._whose_turn:
                        self._direction = [-1, -1]  # set the direction of the move
                        return True

            # must be direct north movement if this line is reached
            else:
                if moving_piece.get_piece_N() == self._whose_turn:
                    self._direction = [-1, 0]  # set the direction of the move
                    return True

        # direct east movement
        elif end[0] == start[0] and end[1] > start[1]:
            if moving_piece.get_piece_E() == self._whose_turn:  # stone in the east position?
                self._direction = [0, 1]  # set direction of the move
                return True

        # direct west movement
        elif end[0] == start[0] and end[1] < start[1]:
            if moving_piece.get_piece_W() == self._whose_turn:  # stone in the west position?
                self._direction = [0, -1]  # set direction of the move
                return True

        return False  # not a valid direction of movement

    def valid_distance(self, start, end):
        """
        Checks whether the distance of a requested move is valid.
        This is determined by whether the piece has a center stone and the attempted distance.
        If the piece has no center stone, only a distance of 3 is allowed.
        If the piece has a center stone, any distance is allowed.
        If distance is valid, the distance attribute is set.
        :param start: the starting coordinate of the piece to be moved (list of two integers)
        :param end: the ending coordinate of the piece to be moved (list of two integers)
        :return: True if distance of requested move is valid; False if distance of requested move is invalid
        """
        # make a piece object
        moving_piece = Piece(start, self._board.get_game_board())

        # if there is a stone in the center of the piece, any distance is valid
        if moving_piece.get_piece_center() == self._whose_turn:
            if end[0] != start[0]:
                self._distance = abs(end[0] - start[0])  # set distance based on vertical movement

            elif end[1] != start[1]:
                self._distance = abs(end[1] - start[1])  # set distance based on horizontal movement

            return True

        # if there is no stone in the center of the piece, the move-distance cannot be greater than 3
        else:
            if abs(end[0] - start[0]) > 3 or abs(end[1] - start[1] > 3):
                # the requested move-distance is greater than 3, but no stone in center of piece
                return False

            if end[0] != start[0]:
                self._distance = abs(end[0] - start[0])  # set distance based on vertical movement
            elif end[1] != start[1]:
                self._distance = abs(end[1] - start[1])  # set distance based on horizontal movement

            return True

    def board_step(self, start, end):
        """
        This method steps across the board in the direction and distance of the desired move, checking at each step
        whether the requested move is obstructed. When only one step is left, the piece is added to the board in its
        final destination, overwriting whatever is there.
        A spot is checked for obstructions by making piece object and then confirming that the piece is empty.
        If movement is obstructed, the move is not made.
        If a the player who made the move broke their own last ring, the board is returned to its previous state.
        :param start: the starting coordinate of the piece to be moved (list of two integers)
        :param end: the ending coordinate of the piece to be moved (list of two integers)
        :return: True if the move was unobstructed and executed; False if the move was obstructed and not executed
        """
        # make a copy of the piece to be moved and remove it from the board
        moving_piece = Piece(start, self._board.get_game_board())
        self._board.remove_piece(start)

        # go in the direction of the move, one step at a time, checking for obstructions at each step
        moving_coordinate = start[:]
        while self._distance > 1:
            # move the coordinate to the next check-position
            moving_coordinate[0] += self._direction[0]
            moving_coordinate[1] += self._direction[1]

            check_piece = Piece(moving_coordinate, self._board.get_game_board())
            if not check_piece.is_empty():  # if the "piece" has any stones, then the path of the move is obstructed
                self._board.add_piece(moving_piece, start)  # return the piece to its starting position
                return False

            self._distance -= 1

        if self.still_in(self._board, moving_piece):  # if the mover didn't break their own last ring
            self._board.add_piece(moving_piece, end)  # add the piece, overwriting the contents of the board
            self._whose_turn, self._up_next = self._up_next, self._whose_turn  # update whose turn it is
            self.still_in_double_check(self._board)  # update game_state if necessary
            return True

        else:
            # return the board to its previous state
            self._board.add_piece(moving_piece, start)

            return False

    def still_in(self, game_board, moving_piece):
        """
        Checks if each player is still in the game.
        This is done by making a piece object at each valid spot on the board and checking for a ring.
        Changes game_state if the player who made the move breaks the other player's last ring.
        This version of the function is called before a move is finalized (piece not yet placed in final destination).
        :param game_board: a board object
        :return: True if the player who made the move is still in, False otherwise.
        """

        def check_piece(color, moving_piece=None):
            """
            Makes a temporary piece at each valid spot on the board, checking if the piece is a ring.
            :param color: color of the player being checked
            :param moving_piece: saves active player's moving piece so that if it's a ring the function will return True
            :return: True if the player has a ring; False if the player has no ring
            """
            if moving_piece and moving_piece.is_ring(color):  # if active player is moving their ring
                return True
            for row in range(3, 19):
                for column in range(3, 19):  # for every square on the board where rings are possible
                    ring_check = Piece([row, column], game_board.get_game_board())  # make a piece
                    if ring_check.is_ring(color):  # check if the piece is a ring
                        return True
            return False

        if check_piece(self._whose_turn, moving_piece):  # if the move didn't break the mover's own last ring
            if not check_piece(self._up_next):  # if the move broke the opponent's last ring
                # change game_state accordingly
                if self._whose_turn == "B":
                    self._game_state = "BLACK_WON"
                else:
                    self._game_state = "WHITE_WON"

            return True

        else:

            return False

    def still_in_double_check(self, game_board):
        """
        Checks if each player is still in the game.
        This is done by making a piece object at each valid spot on the board and checking for a ring.
        Changes game_state if the player who made the move breaks the other player's last ring.
        This version of the function is called after a move is finalized (piece placed in final destination).
        This is because the ring of the opponent won't be broken until the moving piece is finally set.
        :param game_board: a board object
        :return: True if the player who made the move is still in, False otherwise.
        """

        def check_piece(color):
            """
            Makes a temporary piece at each valid spot on the board, checking if the piece is a ring.
            :param color: color of the player being checked
            :return: True if the player has a ring; False if the player has no ring
            """
            for row in range(3, 19):
                for column in range(3, 19):  # for every square on the board where rings are possible
                    ring_check = Piece([row, column], game_board.get_game_board())  # make a piece
                    if ring_check.is_ring(color):  # check if the piece is a ring
                        return True
            return False

        if check_piece(self._up_next):  # if the move didn't break the mover's own last ring
            if not check_piece(self._whose_turn):  # if the move broke the opponent's last ring
                # change game_state accordingly
                if self._whose_turn == "W":
                    self._game_state = "BLACK_WON"
                else:
                    self._game_state = "WHITE_WON"

            return True

        else:

            return False
