import random
import copy
def run():
    while True:
        print("welcome to sodoku!\n chioce the level ! ")
        chioces = ["1-easy", "2-medium", "3-hard","4-end the program"]
        print("\n".join(chioces))
        chioce = handle_errors("please enter chioce from 1 to 4:", 1, 4)
        if chioce==1:
            easy()
        if chioce==2:
            medium()
        if chioce==3:
            hard()
        elif chioce==4:
            print("program ended")
            break

def handle_errors(msg,start=0,end=0):
    while True :
        inp=input(msg)
        if not inp.isdecimal() :
            print("invalid input  try again!")
        elif not ( start<=int(inp)<=end ):
            print("out of range please try again!")
        else :
            return int(inp)

def sudoku_table ():
    arr=[[1,7,9,4,2,5,3,8,6]]  # to generate  sodouku table
    for i in range (1,9):
        arr.append(arr[0][9 - i:] + arr[0][:9 - i])
    random.shuffle(arr)
    return arr

def easy ():
    solution = sudoku_table()
    board = copy.deepcopy(solution)
    for i in range (9):
        board[i][board[i].index(i+1)]=" "
        if i %2==0:
            board[i][i] = " "
        if i <7:
            board[i][random.randint(i+1, 8)] = " "
    printing(board, solution)

def medium():
    solution = sudoku_table()
    board = copy.deepcopy(solution)
    for i in range (9):
        board[i][board[i].index(i+1)]=" "
        if i <7:
            board[i][random.randint(i+1, 8)] = " "
        if i %2==0:
            board[i][:random.randint(7-i, 8)]=" "

    printing(board,solution)

def hard ():
    solution = sudoku_table()
    board = copy.deepcopy(solution)
    for i in range (9):
        if i %2!=0:
            board[i][:random.randint(7-i, 8)]=" "
        if  i <5 and i %2==0:
            board[i][random.randint(3,7):] = " "
        elif i >= 5 and i % 2 == 0:
             board[i][:5] = " "
    printing(board, solution)


def printing(board,solution):
    for i in board:
        print(*i)
    chio=handle_errors("if you want solution enter 1 :",1,1)
    if chio ==1:
        for i in solution:
            print(*i)
if __name__=="__main__":
    run()






