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

# Detailed Explanation

### 1. Imports and Initialization:
The `math` module is imported for using `inf` (infinity) in the `Minimax algorithm`.
The game board is initialized as a list of 9 spaces, representing the 3x3 grid.
Symbols for the human player `('X')` and the AI player `('O')` are defined.

### 2. Function printBoard():
This function prints the current state of the game board.

### 3. Function getEmptyCells():
This function returns a list of indices of empty cells on the board.

### 4. Function isWinner():
This function checks if the given player has won the game by examining all possible winning combinations.

### 5. Function isBoardFull():
This function checks if the game board is full.

### 6. Function evaluate():
This function evaluates the board state and returns a score: 1 if the AI wins, -1 if the human wins, and 0 otherwise.

### 7. Function minimax():
This function implements the Minimax algorithm with alpha-beta pruning to find the optimal move for the AI. It recursively explores all possible moves and assigns scores based on the game outcome.

### 8. Function findBestMove():
This function uses the minimax function to find and return the best move for the AI.

### 9. Function playGame():
This function manages the game play loop, prompting the user for moves, switching turns, and checking for a winner or draw.

# Usage:
Run the program to start a game of Tic Tac Toe.
Choose who will go first: the human player or the AI.
Make moves by entering positions (1-9) on the board.
The game continues until there is a winner or the board is full, resulting in a draw. The program announces the result accordingly.
