class Board():
    def __init__(self):
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        
        return
    
    def get_list(self):
        return self.board
    def set(self, y , x , val):
        self.board[y][x] = val

def play(pos, character, current_board):
    current_board_state = current_board.board
    pos = int(pos)
    if pos == range(10):
        print(pos)
    pairs = {7: [2, 0], 8: [2, 1], 9: [2, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             1: [0, 0], 2: [0, 1], 3: [0, 2]}
    print(pairs[pos])
    print(pairs.get(pos))
    pair = pairs[pos]
    x = pair[0]
    y = pair[1]
    
    print(str(x) + " and " + str(y))
    if (current_board_state[x][y] == 'X') or (current_board_state[x][y] == "Y"):
        print("Invalid Space")
        return current_board
    current_board.set(x,y,character)
    print(character)
    print(current_board.board)
    return current_board


def check_win(board):
    winner = False
    # Horizontal
    for i in board.board:
        if (i[0] == i[1]) and (i[0] == i[2]) and (i[1] == i[2] and (i[1] != ".")):
            print(i[0] + " winner")
            winner = True
    # Vertical
    
    for x in range(3):
        verticals = []
        for y in range(3):
            verticals.append(board.board[y][x])
        print(verticals)
        if (verticals[0] == verticals[1] == verticals[2]):
            print(verticals + " winner")
            winner = True
    
    cross_one_list = [board.board[0][0], board.board[1][1], board.board[2][2]]
    cross_two_list = [board.board[0][2], board.board[1][1], board.board[2][0]]
    # Cross
    if cross_one_list[0] == cross_one_list[1] == cross_one_list[2]:
        print(i[0] + " winner")
        winner = True
    
    if cross_two_list[0] == cross_two_list[1] == cross_two_list[2]:
        print(i[0] + " winner")
        winner = True
    return winner


class main():
    def start_game(self):
        board = Board()
        win = False
        while (win == False):
            x = input("Where would you like to go X?")
            board = play(x, "X", board)
            win = check_win(board)
            if win == True:
                break
            ##Turn for O
            o = input("Where would you like to go O?")
            board = play(o, "O", board)
            win = check_win(board)
        print("Congrats winner")


Game = main()
Game.start_game()
