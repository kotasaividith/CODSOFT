import math

# Initialize the game board as a list of 9 spaces
gameBoard = [' ' for _ in range(9)]
humanPlayer = 'X'
aiPlayer = 'O'

def printBoard(board):
    """
    Prints the current state of the game board.
    
    Parameters:
    board (list): The current game board.
    """
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))

def getEmptyCells(board):
    """
    Returns a list of indexes of empty cells in the board.
    
    Parameters:
    board (list): The current game board.
    
    Returns:
    list: List of indexes of empty cells.
    """
    return [i for i, cell in enumerate(board) if cell == ' ']

def isWinner(board, player):
    """
    Checks if the given player has won the game.
    
    Parameters:
    board (list): The current game board.
    player (str): The player symbol ('X' or 'O').
    
    Returns:
    bool: True if the player has won, False otherwise.
    """
    winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in winningCombinations)

def isBoardFull(board):
    """
    Checks if the game board is full.
    
    Parameters:
    board (list): The current game board.
    
    Returns:
    bool: True if the board is full, False otherwise.
    """
    return ' ' not in board

def evaluate(board):
    """
    Evaluates the game board and returns a score.
    
    Parameters:
    board (list): The current game board.
    
    Returns:
    int: 1 if the AI has won, -1 if the human player has won, 0 otherwise.
    """
    if isWinner(board, aiPlayer):
        return 1
    elif isWinner(board, humanPlayer):
        return -1
    else:
        return 0    

def minimax(board, depth, alpha, beta, maximizingPlayer):
    """
    Implements the Minimax algorithm with alpha-beta pruning.
    
    Parameters:
    board (list): The current game board.
    depth (int): The current depth of the recursion.
    alpha (int): The best value that the maximizer can guarantee.
    beta (int): The best value that the minimizer can guarantee.
    maximizingPlayer (bool): True if the current move is for the maximizer (AI), False if for the minimizer (human).
    
    Returns:
    int: The evaluation score for the current board state.
    """
    if depth == 0 or isWinner(board, humanPlayer) or isWinner(board, aiPlayer) or isBoardFull(board):
        return evaluate(board)

    if maximizingPlayer:
        maxVal = -math.inf
        for cell in getEmptyCells(board):
            board[cell] = aiPlayer
            val = minimax(board, depth - 1, alpha, beta, False)
            board[cell] = ' '
            maxVal = max(maxVal, val)
            alpha = max(alpha, maxVal)
            if beta <= alpha:
                break
        return maxVal
    else:
        minVal = math.inf
        for cell in getEmptyCells(board):
            board[cell] = humanPlayer
            val = minimax(board, depth - 1, alpha, beta, True)
            board[cell] = ' '
            minVal = min(minVal, val)
            beta = min(beta, minVal)
            if beta <= alpha:
                break
        return minVal

def findBestMove(board):
    """
    Finds the best move for the AI player.
    
    Parameters:
    board (list): The current game board.
    
    Returns:
    int: The index of the best move.
    """
    bestVal = -math.inf
    bestMove = -1
    alpha = -math.inf
    beta = math.inf
    for cell in getEmptyCells(board):
        board[cell] = aiPlayer
        val = minimax(board, 9, alpha, beta, False)
        board[cell] = ' '
        if val > bestVal:
            bestVal = val
            bestMove = cell
        alpha = max(alpha, bestVal)
    return bestMove
    
def playGame():
    """
    Manages the game play loop.
    """
    print("Who will play the first move? Select: 1. Me  2. AI")
    option = int(input("Enter the option: "))
    currentPlayer = humanPlayer if option == 1 else aiPlayer

    while not isWinner(gameBoard, humanPlayer) and not isWinner(gameBoard, aiPlayer) and not isBoardFull(gameBoard):
        if currentPlayer == humanPlayer:
            print("Your turn (", humanPlayer, ")")
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in getEmptyCells(gameBoard):
                print("Invalid move, try again.")
                continue
        else:
            print("AI's turn (", aiPlayer, ")")
            move = findBestMove(gameBoard)
        
        gameBoard[move] = currentPlayer
        printBoard(gameBoard)
        currentPlayer = humanPlayer if currentPlayer == aiPlayer else aiPlayer

     if isWinner(gameBoard, playerHuman):
        print("you wint the game 👑")
    elif isWinner(gameBoard, playerAI):
        print("bot wins the game 🤭")
    else:
        print("a draw 😏")

# Start the game
print("_____Tic Tac Toe_____")
print("Initial board:")
printBoard(gameBoard)
playGame()
