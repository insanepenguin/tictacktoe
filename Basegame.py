
class Board():
    def __init__(self):
        self.board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

        return
    def get_list(self):
        return self.board
def play(pos,character,current_board):

    print(current_board)
    return current_board

def check_win(board):
    print()
    #Horizontal
    ##[[S,S,S]
    ##[S,S,S]
    ##[S,S,S]]

    # for i in board.board:
    #     if (i[0] == i[1] ) and (i[0] == i[2]) and (i[1] == i[2] and (i[1] != ".")):
    #         print(i[0] + " winner")
    #         winner = True
    # #Vertical
    # print(board.board)
    # ver_One_list = [board.board[0][0],board.board[0][1],board.board[0][2]]
    # ver_Two_list = [board.board[1][0],board.board[1][1],board.board[1][2]]
    # ver_Three_list = [board.board[2][0],board.board[2][1],board.board[2][2]]
    # print(ver_One_list)
    # print(ver_Two_list)
    # print(ver_Three_list)
    # if ver_One_list[0] == ver_One_list[1] == ver_One_list[2]:
    #     print(i[0] + " winner")
    #     winner = True
    #
    # if ver_Two_list[0] == ver_Two_list[1] == ver_Two_list[2]:
    #     print(i[0] + " winner")
    #     winner = True
    #
    # if ver_Three_list[0] == ver_Three_list[1] == ver_Three_list[2]:
    #     print(i[0] + " winner")
    #     winner = True
    # cross_one_list = [board.board[0][0],board.board[1][1],board.board[2][2]]
    # cross_two_list = [board.board[0][2],board.board[1][1],board.board[2][0]]
    # if cross_one_list[0] == cross_one_list[1] == cross_one_list[2]:
    #     print(i[0] + " winner")
    #     winner = True
    #
    # if cross_two_list[0] == cross_two_list[1] == cross_two_list[2]:
    #     print(i[0] + " winner")
    #     winner = True
    # return

class main():
    def start_game(self):
        board = Board()
        win = False
        while(win == False):
            x = input("Where would you like to go X?")
            play(x,"X",board)
            win = check_win(board)
            if win == True:
                break
            ##Turn for O
            o = input("Where would you like to go O?")
            play(o,"O",board)
            win = check_win(board)
        print("Congrats winner")


Game = main()
Game.start_game()