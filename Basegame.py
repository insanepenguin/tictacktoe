
class Board():
    def __init__(self, list):
        self.board = []
        print(len(list))
        if len(list) != 9:
            print("Bad board State exiting program")
            exit(0)
            return
        else:
            self.board = list
        return
    def get_list(self):
        return self.board
def play(pos,character,current_board):
    new_int = -4
    if character == "X":
        new_int = -1
    elif character == "O":
        new_int = 1
    else:
        new_int = -1000
        print("Error in executing the play Exiting")
        exit(0)
        return
    pos = pos - 1
    current_board[pos] = new_int
    print(current_board)
    return current_board

def check_win(board):
    board_state=board.get_list()
    v1 = [0, 3, 6]
    v2 = [1, 4, 7]
    v3 = [2, 5, 8]
    h1 = [0, 1, 2]
    h2 = [3, 4, 5]
    h3 = [6, 7, 8]
    d1 = [0, 4, 8]
    d2 = [6, 4, 2]
    combos = [v1, v2, v3, h1, h2, h3, d1, d2]


    for list in combos:
        print(list)
        sum = 0
        for x in list:
            sum = sum + board_state[x]
            #print(sum)
        if sum == -3:
            print("X wins")

            return True
        if sum == 3:
            print("Y wins")

            return True
    return False



class main():
    def start_game(self):
        board = Board([0,0,0,0,0,0,0,0,0])
        win = False
        while(win == False):
            number = input("Player 1 place your X by using the numbers 1-9")
            character = "X"
            board =Board(play(int(number),character,board.get_list()))
            print(board.get_list())
            win = check_win(board)
            if win == True:
                break
            number = input("Player 2 place your X by using the numbers 1-9")
            character = "O"
            board = Board(play(int(number), character, board.get_list()))
            print(board.get_list())
            win = check_win(board)
        print("Congrats winner")
        exit(0)

Game = main()
Game.start_game()