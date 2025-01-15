"""
8. Tic-Tac-Toe
◦ Features: Two-player mode and input validation.
◦ Key Concepts: Lists, nested loops, conditionals.
"""

def main():
    x_value = 'X'
    o_value = 'O'

    dict_tic_ui = {'top_left': "#", 'top_middle': "#", 'top_right':"#",
            'middle_left': "#", 'middle_middle': "#", "middle_right": "#",
            'bottom_left': "#", 'bottom_middle':"#", 'bottom_right': "#"}
    
    print(f"\n{dict_tic_ui['top_left']}|{dict_tic_ui['top_middle']}|{dict_tic_ui['top_right']}\n{dict_tic_ui['middle_left']}|{dict_tic_ui['middle_middle']}|{dict_tic_ui['middle_right']}\n{dict_tic_ui['bottom_left']}|{dict_tic_ui['bottom_middle']}|{dict_tic_ui['bottom_right']}")

    

main()