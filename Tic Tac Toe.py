# Making a Game of Tic Tac Toe
# First Thing I Will Do is Make the Board by using list, and for-in statement
PLAYER_ONE="X"
COMPUTER="O"

def game():
    Tic_Tac_Toe = [[O,O,O],
                   [O,O,O],
                   [O,O,O],]
    for row in Tic_Tac_Toe:
        print(row)
def main():
    game()
main()