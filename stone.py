import pygame
from constants import SQUARE_SIZE, W, B


class Stone:
    PADDING = 10
    RADIUS = SQUARE_SIZE // 2 - PADDING

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        if color == "W":
            self.color = W
        else:
            self.color = B
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        pygame.draw.circle(win,
                           self.color,
                           (self.x, self.y),
                           self.RADIUS)
