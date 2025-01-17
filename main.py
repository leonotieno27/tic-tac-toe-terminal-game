# Dictionary for the board
dict_tic_ui = {1: " ", 2: " ", 3: " ",
               4: " ", 5: " ", 6: " ",
               7: " ", 8: " ", 9: " "}

x_value = 'X'
o_value = 'O'
winning_combinations = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9), 
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  
    (1, 5, 9), (3, 5, 7)             
]

def board():
    """Prints the game board."""
    print(f"\n{dict_tic_ui[1]}|{dict_tic_ui[2]}|{dict_tic_ui[3]}")
    print("-+-+-")
    print(f"{dict_tic_ui[4]}|{dict_tic_ui[5]}|{dict_tic_ui[6]}")
    print("-+-+-")
    print(f"{dict_tic_ui[7]}|{dict_tic_ui[8]}|{dict_tic_ui[9]}")

def check_winner(turn):
    """Checks if the current player has won."""
    for combo in winning_combinations:
        if dict_tic_ui[combo[0]] == dict_tic_ui[combo[1]] == dict_tic_ui[combo[2]] == turn:
            return True
    return False

turn = x_value
for i in range(9):
    print(f"Turn for {turn}. Move on which space?")
    move = int(input())
    if 1 <= move <= 9:
        if dict_tic_ui[move] == " ":
            dict_tic_ui[move] = turn
            board()
            if check_winner(turn):
                print(f"Player {turn} wins!")
                break
            # Switch turns
            turn = o_value if turn == x_value else x_value
        else:
            print("That space is already taken.")
    else:
        print("Invalid input. Please choose a number between 1 and 9.")
else:
    print("It's a draw!")
