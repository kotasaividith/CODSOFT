# Tic Tac Toe Program Description
This Tic Tac Toe program is a command-line implementation of the classic game where a human player competes against an AI. The AI uses the Minimax algorithm with alpha-beta pruning to make optimal moves. The game is played on a 3x3 grid, and the goal is to get three of your symbols (either 'X' or 'O') in a row, column, or diagonal.

## Key Components
### Game Board:
Represented as a list of 9 elements, initially filled with spaces (' '), corresponding to the 3x3 grid.

### Players:
Human player ('X')
AI player ('O')

### Core Functions:
printBoard(board): Displays the current state of the game board.
getEmptyCells(board): Returns a list of indices of empty cells on the board.
isWinner(board, player): Checks if the given player has won the game.
isBoardFull(board): Checks if the game board is full.
evaluate(board): Evaluates the board state and returns a score based on who is winning.
minimax(board, depth, alpha, beta, maximizingPlayer): Implements the Minimax algorithm with alpha-beta pruning to find the optimal move.
findBestMove(board): Uses the Minimax function to find and return the best move for the AI.
playGame(): Manages the game play loop, prompting the user for moves, switching turns, and checking for a winner or draw.
