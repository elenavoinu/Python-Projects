#@evoinu
#Complete the PrintTicTacToe function with parameters horiz_char and vert_char 
#that prints a tic-tac-toe board with the characters as follows.
#Ex: print_tic_tac_toe('~', '!') prints:
#                       x ! x ! x
#                       ~ ~ ~ ~ ~
#                       x ! x ! x
#                       ~ ~ ~ ~ ~
#                       x ! x ! x

#''' Your solution goes here '''

def print_tic_tac_toe(horiz_char, vert_char):
    print("x " + vert_char + " x " + vert_char + " x" )
    print(horiz_char + " " + horiz_char + " " + horiz_char + " " + horiz_char+ " " + horiz_char)
    print("x " + vert_char + " x " + vert_char + " x" )
    print(horiz_char + " " + horiz_char + " " + horiz_char + " " + horiz_char+ " " + horiz_char)
    print("x " + vert_char + " x " + vert_char + " x" )

print_tic_tac_toe('~', '!')
