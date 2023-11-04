# Game and game logic

class CPU:
    evaluation_values = {
        "X": 1,
        "Tie": 0,
        "O": -1
    }

    def __init__(self, player):
        # self.player is the ai
        self.player = player
        self.infinity = float("inf")
        self.negative_infinity = float("-inf")
    
    def possibleMoves(self, board):
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    empty_cells.append((row, col))
        return empty_cells

    def getMove(self, board):
        empty_cells = self.possibleMoves(board)
        if self.player == "X":
            best_value = self.negative_infinity
            best_move = empty_cells[0]
            for move in empty_cells:
                board[move[0]][move[1]] = self.player
                value = self.minimax(board, 9, "O")
                board[move[0]][move[1]] = " "
                if value > best_value:
                    best_value = value
                    best_move = move
        elif self.player == "O":
            best_value = self.infinity
            best_move = empty_cells[0]
            for move in empty_cells:
                board[move[0]][move[1]] = self.player
                value = self.minimax(board, 9, "X")
                board[move[0]][move[1]] = " "
                if value < best_value:
                    best_value = value
                    best_move = move
        return best_move

    def minimax (self, board, depth, player):
        if depth == 0 or TicTacToe.checkWin(board):
            return self.evaluation_values[TicTacToe.checkWin(board)]
        
        children = self.possibleMoves(board)
        
        if player == "X":
            value = self.negative_infinity
            for child in children:
                board[child[0]][child[1]] = player
                value = max(value, self.minimax(board, depth - 1, "O"))
                board[child[0]][child[1]] = " "
            return value
        else:
            value = self.infinity
            for child in children:
                board[child[0]][child[1]] = player
                value = min(value, self.minimax(board, depth - 1, "X"))
                board[child[0]][child[1]] = " "
            return value

class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.currentPlayer = "X"
        
    def displayBoard(self):
        print(self.board[0][0] + "  | " + self.board[0][1] + " | " + self.board[0][2])
        print("---+---+---")
        print(self.board[1][0] + "  | " + self.board[1][1] + " | " + self.board[1][2])
        print("---+---+---")
        print(self.board[2][0] + "  | " + self.board[2][1] + " | " + self.board[2][2])

    def isMoveValid(self, row, col):
        if self.board[row][col] == " ":
            return True
        else:
            return False
        
    @staticmethod   
    def checkWin(board):
        # Note to self: try to make this section cleaner

        # Check Rows
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        # Check Columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return board[0][i]
        # Check Diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        
        # Check for tie
        tie = True
        for row in board:
            for cell in row:
                if cell == " ":
                    tie = False
        if tie:
            return "Tie"
        
        return False

    def gameLoopPvP(self):

        # Game Loop
        while not self.checkWin(self.board):
            self.displayBoard()
            print("It is " + self.currentPlayer + "'s turn.")
            # Collect Move
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            # Attempt to make move
            if self.isMoveValid(row, col):
                self.board[row][col] = self.currentPlayer
            else:
                print("Invalid move! Please retry.")
                continue
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"
            
        # Display win state
        self.displayBoard()
        if self.checkWin(self.board) == "Tie":
            print("It's a tie!")
        else:
            print(self.checkWin(self.board) + " wins!")
    
    def gameLoopPvAI(self, userPlayer):

        # Initialize AI
        if userPlayer == "X":
            aiPlayer = "O"
        elif userPlayer == "O":
            aiPlayer = "X"
        else:
            print("Invalid player! Please retry.")
            return
        ai = CPU(aiPlayer)

        # Game Loop
        while not self.checkWin(self.board):
            self.displayBoard()
            print("It is " + self.currentPlayer + "'s turn.")
            #print(AI.Node(self.board, self.currentPlayer))
            # Collect Moves
            if self.currentPlayer == userPlayer:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
            else:
                row, col = ai.getMove(self.board)
            # Attempt to make move
            if self.isMoveValid(row, col):
                self.board[row][col] = self.currentPlayer
            else:
                print("Invalid move! Please retry.")
                continue
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"

        # Display win state
        self.displayBoard()
        if self.checkWin(self.board) == "Tie":
            print("It's a tie!")
        else:
            print(self.checkWin(self.board) + " wins!")
    
    def gameLoopAIvAI(self):

        # Initialize AI
        aiX = CPU("X")
        aiO = CPU("O")

        # Game Loop
        while not self.checkWin(self.board):
            self.displayBoard()
            print("It is " + self.currentPlayer + "'s turn.")
            #print(AI.Node(self.board, self.currentPlayer))
            # Collect Moves
            if self.currentPlayer == "X":
                row, col = aiX.getMove(self.board)
            else:
                row, col = aiO.getMove(self.board)
            # Attempt to make move
            if self.isMoveValid(row, col):
                self.board[row][col] = self.currentPlayer
            else:
                print("Invalid move! Please retry.")
                continue
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"

        # Display win state
        self.displayBoard()
        if self.checkWin(self.board) == "Tie":
            print("It's a tie!")
        else:
            print(self.checkWin(self.board) + " wins!")
