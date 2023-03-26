import random

board = [' ']*9

# Write a function print_board(board) that prints the board in a nice way

def is_all_full(board):
    for i in range(0,9,1):
        if board[i] == ' ':
            return False
    return True

def check_game(eval):
    if eval >= 100:
        print("You lose")
        return 1
    elif eval <= -100:
        print("You win")
        return -1
    else:
        #print(board)
        if(is_all_full(board) == True):
            print("Draw")
            return 0
        else:
            return 2

def print_board(board_input):
    print("-------------")
    print("|", board_input[0], "|", board_input[1], "|", board_input[2], "|")
    print("-------------")
    print("|", board_input[3], "|", board_input[4], "|", board_input[5], "|")
    print("-------------")
    print("|", board_input[6], "|", board_input[7], "|", board_input[8], "|")
    print("-------------")

def calc_eval():
    res = 0
    ways_to_win = [[0,1,2],
                   [3,4,5],
                   [6,7,8],
                   [0,3,6],
                   [1,4,7],
                   [2,5,8],
                   [0,4,8],
                   [2,4,6]]
    countx = 0
    counto = 0
    for rows in ways_to_win:
        countx = 0
        counto = 0
        for slot in rows:
            if board[rows[0]] == board[rows[1]] == board[rows[2]] == 'X':
                res += 100
            if board[rows[0]] == board[rows[1]] == board[rows[2]] == 'O':
                res -= 100
            if board[slot] == 'X':
                countx += 1
            if board[slot] == 'O':
                counto += 1
        if countx > counto:
            res += int(10**((countx - counto) - 1))
        elif counto > countx:
            res -= int(10**((counto - countx) - 1))
        else:
            continue
    return res

def check_valid(move):
    return board[int(move)] == ' '

def calc_state():
    global board
    return (board, calc_eval())

def print_result(check):
    if check == 1:
        print("You lose")
    elif check == -1:
        print("You win")
    else:
        print("Draw")
# 

def play():
    global board
    board[random.randint(0,8)] = 'X'
    state = calc_state()
    #print_board(state[0])
    print_board(calc_state()[0])
    print("Current Heuristic: ", calc_state()[1])

    while True:

        if check_game(calc_state()[1]) != 2:
            return

        while True:
            s = input("Enter your move: ")
            if check_valid(int(s)-1):
                board[int(s)-1] = 'O'
                break
            else:
                print("Incorrect move. Try again")

        print_board(board)
        #print("Current Heuristic: ", calc_state()[1])

        if check_game(calc_state()[1]) != 2:
            return

        print('Computer is thinking...')
        ranges = []
        for i in range(0,9,1):
            if(board[i] == ' '):
                board[i] = 'X'
                copy = []
                for j in range(0,9,1):
                    copy.append(board[j])
                ranges.append((copy, calc_eval()))
                board[i] = ' '
        max_state = (None, -1)
        for states in ranges: 
            if states[1] > max_state[1]:
                max_state = states
        board = max_state[0]
        print_board(board)
        print("Current Heuristic: ", max_state[1])

play()
