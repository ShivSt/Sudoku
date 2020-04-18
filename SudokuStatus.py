import time

board=[]
"""
board.append([2,9,5,7,4,3,8,6,1])
board.append([4,3,1,8,6,5,9,2,7])
board.append([8,7,6,1,9,2,5,4,3])
board.append([3,8,7,4,5,9,2,1,6])
board.append([6,1,2,3,8,7,4,9,5])
board.append([5,4,9,2,1,6,7,3,8])
board.append([7,6,3,5,2,4,1,8,9])
board.append([9,2,8,6,7,1,3,5,4])
board.append([1,5,4,9,3,8,6,7,2])
"""

#displaySudoku(board)
def displaySudoku(board):
    for i in range(9):
        print("""
+---+---+---+---+---+---+---+---+---+""")
        for elem in board[i]:
            print("|",elem,end=" ")
        print("|",end="")
    print("""
+---+---+---+---+---+---+---+---+---+""")

    
#Check status of sudoku if it is valid?
def verifySudoku(board):
    
    for i in range(9):
        for elem in board[i]:
            if board[i].count(elem)>1: 
                return "No"

    for i in range(9):
        lst=[]
        for j in range(9):
            lst.append(board[j][i])
        for elem in lst:
            if lst.count(elem)>1: 
                return "No"

    for i in range(3):
        for j in range(3):
            list1=[]
            for k in range(i*3,3+i*3):
                for l in range(j*3,3+j*3):
                    list1.append(board[k][l])
            for elem in list1:
                if list1.count(elem)>1:
                    return "No"
    
    return "Yes"

              
#Test Data
"""  
board.append([1,2,3,4,5,6,7,8,9])
board.append([2,3,4,5,6,7,8,9,1])
board.append([3,4,5,6,7,8,9,1,2])
board.append([4,5,6,7,8,9,1,2,3])
board.append([5,6,7,8,9,1,2,3,4])
board.append([6,7,8,9,1,2,3,4,5])
board.append([7,8,9,1,2,3,4,5,6])
board.append([8,9,1,2,3,4,5,6,7])
board.append([9,1,2,3,4,5,6,7,8])
"""
board.append([1,9,5,7,4,3,8,6,2])
board.append([4,3,1,8,6,5,9,2,7])
board.append([8,7,6,1,9,2,5,4,3])
board.append([3,8,7,4,5,9,2,1,6])
board.append([6,1,2,3,8,7,4,9,5])
board.append([5,4,9,2,1,6,7,3,8])
board.append([7,6,3,5,2,4,1,8,9])
board.append([9,2,8,6,7,1,3,5,4])
board.append([2,5,4,9,3,8,6,7,1])

displaySudoku(board)

print(verifySudoku(board))

time.sleep(6)
quit
