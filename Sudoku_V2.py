board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):

    #Check the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: #Check entire row for same number except the spot we put the new num in
            return False


    #Check column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check Square
    x_box = pos[1]//3       #To understand which position we are currently on
    y_box = pos[0]//3

    for i in range(y_box*3,y_box*3+3):          #Multiply to cancel the division that we did to find the 3*3 box
        for j in range(x_box*3,x_box*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True    #If all of the above tests fail, return True

def print_board(bo):

    for i in range(len(bo)):
        if i%3 == 0 and i!=0:   #print horizontal lines every 3rd line
            print('---------+----------+---------')
        for j in range(len(bo)):
            if j%3 == 0 and j!=0:
                print('| ', end='')
            if j == 8:
                print(bo[i][j]) #Needs to go to the next line after the last element so no end=''
            else:
                print(str(bo[i][j]),' ', end='')    #Not the last element so has to stay in the same line

def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j]==0:
                return (i,j)  #Return row,column index

    return None #Return None if there are no empty spaces the whole puzzle has been solved)






print('The Question is :')
print('')
print_board(board)
print('')
print('---------------------')
print('0 denotes blank boxes')
print('---------------------')
solve(board)
print('')
print('***Solving***')
print('')
import time #for asthetics only
time.sleep(2)
print('The solved sudoku is')
print('')


print_board(board)
