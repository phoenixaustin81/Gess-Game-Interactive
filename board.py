class Board:
    """
    The Board class has one data member: the board of a GessGame object.
    The GessGame class uses Board class methods and data member.
    The Board class manages the state of the game board by adding and removing game Piece objects.
    The Board class needs to communicate with a the Piece class in order to add a Piece, but removing a Piece can be
    done without communication with the Piece class.
    """

    def __init__(self):
        """
        Initializes the board data member of the board class.
        The board is a list of lists.
        The top row and left column are completely inaccessible to the GessGame class, and are only there for playing
        purposes.
        """
        self._board = [
            [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
            [20, '  ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [19, '  ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', ' '],
            [18, '  ', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', ' '],
            [17, '  ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', ' '],
            [16, '  ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [15, '  ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [14, '  ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' '],
            [13, '  ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [12, '  ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [11, '  ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [10, '  ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [9, '   ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [8, '   ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [7, '   ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' '],
            [6, '   ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [5, '   ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [4, '   ', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
            [3, '   ', 'B', 'B', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', ' '],
            [2, '   ', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
            [1, '   ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def get_game_board(self):
        """
        :return: board data member (list of lists)
        """
        return self._board

    def remove_piece(self, location):
        """
        Removes a piece centered at the coordinates specified by the input parameter.
        The center and all surrounding "squares" are filled with a string of one space, which indicates no stone.
        :param location: list of two integers indicating location on the board
        """
        self._board[location[0]][location[1]] = ' '
        self._board[location[0] + 1][location[1]] = ' '
        self._board[location[0] + 1][location[1] + 1] = ' '
        self._board[location[0] + 1][location[1] - 1] = ' '
        self._board[location[0]][location[1] + 1] = ' '
        self._board[location[0] - 1][location[1]] = ' '
        self._board[location[0] - 1][location[1] + 1] = ' '
        self._board[location[0] - 1][location[1] - 1] = ' '
        self._board[location[0]][location[1] - 1] = ' '

    def add_piece(self, piece, location):
        """
        Adds the attributes of a Piece object to the board attribute of a Board object.
        The piece is only added if its center is on the board - b to s horizontally and 2 to 19 vertically.
        Piece perimeter attributes are not added if they are off the board,
        but the portion of the perimeter that is on the board is added.
        :param piece: a Piece object
        :param location: list of two integers indicating location on the board
        """
        # if the center of the piece is being added to a valid spot on the board...
        if location[0] in range(2, 20) and location[1] in range(2, 20):
            self._board[location[0]][location[1]] = piece.get_piece_center()

            # then add the center, plus any other part of the piece that is not off the board
            if location[0] - 1 in range(2, 20) and location[1] in range(2, 20):
                self._board[location[0] - 1][location[1]] = piece.get_piece_N()

            if location[0] - 1 in range(2, 20) and location[1] - 1 in range(2, 20):
                self._board[location[0] - 1][location[1] - 1] = piece.get_piece_NW()

            if location[0] - 1 in range(2, 20) and location[1] + 1 in range(2, 20):
                self._board[location[0] - 1][location[1] + 1] = piece.get_piece_NE()

            if location[0] + 1 in range(2, 20) and location[1] in range(2, 20):
                self._board[location[0] + 1][location[1]] = piece.get_piece_S()

            if location[0] + 1 in range(2, 20) and location[1] - 1 in range(2, 20):
                self._board[location[0] + 1][location[1] - 1] = piece.get_piece_SW()

            if location[0] + 1 in range(2, 20) and location[1] + 1 in range(2, 20):
                self._board[location[0] + 1][location[1] + 1] = piece.get_piece_SE()

            if location[0] in range(2, 20) and location[1] + 1 in range(2, 20):
                self._board[location[0]][location[1] + 1] = piece.get_piece_E()

            if location[0] in range(2, 20) and location[1] - 1 in range(2, 20):
                self._board[location[0]][location[1] - 1] = piece.get_piece_W()
