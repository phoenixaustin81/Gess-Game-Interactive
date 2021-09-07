# Gess Board Game

Gess is an abstract board game - a Chess/Go variant. The game is played on a 20x20 Go board, but the perimeter of the board is out of bounds. A game piece is any 3x3 grid with stones of the active player. A valid piece cannot contain stones of the opponent.

Valid direction and distance of movement are determined by the fooprint of stones within a piece. For example, if a piece has a stone in its northeast cell, then the piece is allowed to move northeast. A center stone allows movement of any distance. If the piece does not have a center stone, then it can move no more than three steps in a valid direction.

The goal of the game is to capture the opposing player's ring. Each player starts with one ring, although additional rings can be formed.

Any stone in the path of a piece will be captured, and the moving piece cannot move any further.

For more details on game rules, visit https://www.chessvariants.com/crossover.dir/gess.html.

## Live Demo

Play the game online at https://trinket.io/pygame/0bc99bdb28.
Expand the play-window **left and down** for the best experience.

## Installation

Follow these steps to run the game locally:

1. Install python and pygame
2. Clone the repo: `git clone https://github.com/phoenixaustin81/Gess-Game-Interactive.git`
3. Navigate to the folder where you cloned the repo
4. Play the game: `python main.py` or `python3 main.py`
