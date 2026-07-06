print("this is a tic tac toe game")
board=["1","2","3","4","5","6","7","8","9"]
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

display_board(board)
def check_winner(board):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]   
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]]:
                return board[combination[0]]  # Return the winner ("X" or "O")

        return None  # No winner yet
        

current_player="X"
if current_player=="X":
    print("current player is X")
else:
    print("current player is O")

while True:
    choose=input(f"Player {current_player}, choose a number between 1 to 9 to place your mark: ")
    index=int(choose)-1

    if board[index]=="X" or board[index]=="O":
        print("this place is already taken, choose another number")
    else:
        board[index]=current_player
        display_board(board)
        if current_player=="X":
            current_player="O"
        else:
            current_player="X"


     


        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        else:
            if all(space in ["X", "O"] for space in board):
                print("It's a draw!")
                break
