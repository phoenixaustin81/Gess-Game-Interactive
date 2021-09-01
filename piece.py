class Piece:
    """
    The Piece class has data members for keeping track of where stones are in a GessGame board-piece.
    Piece class methods look at Piece attributes to return relevant information such as if the Piece is a ring or empty.
    Communication with the Board class is required to make a Piece object;
    a Piece object is a copy of a section of board from a Board object.
    """
    def __init__(self, location, board):
        """
        Fills the Piece with stones or spaces depending on the orientation
        of the input Board object and location on the board.
        :param location: list of two integers indicating location on the board
        :param board: a Board object
        """
        self._center = board[location[0]][location[1]]
        self._N = board[location[0] - 1][location[1]]
        self._NW = board[location[0] - 1][location[1] - 1]
        self._NE = board[location[0] - 1][location[1] + 1]
        self._S = board[location[0] + 1][location[1]]
        self._SW = board[location[0] + 1][location[1] - 1]
        self._SE = board[location[0] + 1][location[1] + 1]
        self._W = board[location[0]][location[1] - 1]
        self._E = board[location[0]][location[1] + 1]

        self._piece_matrix = [[self._NW, self._N, self._NE],
                              [self._W, self._center, self._E],
                              [self._SW, self._S, self._SE]]

    def perimeter(self):
        """
        The perimeter method is used by the is_ring method to check if a piece is a ring.
        :return: a list with all attributes of the Piece except the center attribute
        """
        return [self._N, self._NW, self._NE, self._S, self._SW, self._SE, self._W, self._E]

    def is_ring(self, color):
        """
        Checks whether a piece is a ring.
        A ring is a piece with a perimeter of all the same stone, but no center stone.
        :param color: color of the stones of the piece that might be a ring
        :return: True if piece is a ring; False if piece is not a ring
        """
        if self._center == " ":  # can only be a ring if center has no stone
            perimeter_count = 0
            for stone in self.perimeter():
                if stone == color:
                    perimeter_count += 1
            if perimeter_count == 8:  # if every stone in the perimeter is the specified color
                return True
        else:
            return False

    def valid_piece(self, up_next):
        """
        Confirms that a piece does not have stones of the other player.
        :param up_next: color of the player who is not currently authorized to make a move
        :return: True if piece has no stones of the opponent; False otherwise
        """
        if self._center == up_next:
            return False
        if up_next in self.perimeter():
            return False

        return True

    def is_empty(self):
        """
        :return: True if a piece has no stones; False if a piece has a stone
        """
        for row in self._piece_matrix:
            for space in row:
                if space != ' ':  # no stone in the space
                    return False

        return True

    def get_piece_center(self):
        """
        :return: center attribute of the piece
        """
        return self._center

    def get_piece_N(self):
        """
        :return: north attribute of the piece
        """
        return self._N

    def get_piece_NW(self):
        """
        :return: northwest attribute of the piece
        """
        return self._NW

    def get_piece_NE(self):
        """
        :return: northeast attribute of the piece
        """
        return self._NE

    def get_piece_S(self):
        """
        :return: south attribute of the piece
        """
        return self._S

    def get_piece_SW(self):
        """
        :return: southwest attribute of the piece
        """
        return self._SW

    def get_piece_SE(self):
        """
        :return: southeast attribute of the piece
        """
        return self._SE

    def get_piece_W(self):
        """
        :return: west attribute of the piece
        """
        return self._W

    def get_piece_E(self):
        """
        :return: east attribute of the piece
        """
        return self._E
