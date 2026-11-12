def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_tie(board):
    return all(space in ["X", "O"] for space in board)

def play_game():
    board = [str(i + 1) for i in range(9)]
    current_player = "X"
    game_over = False

    print("--- Welcome to Tic-Tac-Toe! ---")
    print("Choose a position from 1 to 9 as shown below:")
    
    while not game_over:
        print_board(board)
        
        try:
            choice = int(input(f"Player {current_player}, choose your position (1-9): ")) - 1
            
            if choice < 0 or choice > 8:
                print("Invalid position! Please pick a number from 1 to 9.")
                continue
            if board[choice] in ["X", "O"]:
                print("That space is already taken! Choose another standard position.")
                continue
                
            board[choice] = current_player
            
            if check_win(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                game_over = True
            elif check_tie(board):
                print_board(board)
                print("🤝 It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
                
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 9.")

if __name__ == "__main__":
    play_game()