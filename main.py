"""
8. Tic-Tac-Toe
◦ Features: Two-player mode and input validation.
◦ Key Concepts: Lists, nested loops, conditionals.
"""

dict_tic_ui = {1: " ", 2: " ", 3: " ",
               4: " ", 5: " ", 6: " ",
               7: " ", 8: " ", 9: " "}

x_value = 'X'
o_value = 'O'  
winning_combinations = [(1,2,3), (4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]


def board(theBoard):  
    print(f"\n{dict_tic_ui[1]}|{dict_tic_ui[2]}|{dict_tic_ui[3]}")
    print("-+-+-")
    print(f"{dict_tic_ui[4]}|{dict_tic_ui[5]}|{dict_tic_ui[6]}")
    print("-+-+-")
    print(f"{dict_tic_ui[7]}|{dict_tic_ui[8]}|{dict_tic_ui[9]}")

turn = x_value
for i in range(9):
    print('Turn for '+ turn + '. Move on which space?')
    move = input()
    move = int(move)
    if move > 0 and move <= 9:
        if dict_tic_ui[move] == " ":
            dict_tic_ui[move] = turn
            board(dict_tic_ui)
            if turn == x_value:
                turn = o_value
            else:
                turn = x_value
        else:
            print("Space already teken")
    else:
        print("Out of range")

  

