from time import sleep
from random import randrange,randint


#Display Sudoku board's current status
def displaySudoku(board):
    for i in range(9):
        print("""
+---+---+---+---+---+---+---+---+---+""")
        for elem in board[i]:
            print("|",elem,end=" ")
        print("|",end="")
    print("""
+---+---+---+---+---+---+---+---+---+""")

#Check If the element is already present in the board against sudoku rule
def checkIfElementduplicates(board,elem,i,j):  
    if board[i].count(elem)>0: #Check in a row elements
        return "Yes"
    l1=[]
    for row in range(9): #Check in a column elements
        l1.append(board[row][j])
    if l1.count(elem)>0:
        return "Yes"
    
    i=i//3
    j=j//3
    list1=[]
    #Check in a square 0f 3*3
    for k in range(i*3,3+i*3):
        for l in range(j*3,3+j*3):
            list1.append(board[k][l])
    if list1.count(elem)>0:
        return "Yes"
    
    else: return "No"


def presetSudoku(board):
    for i in range(9):
        for j in range(9):
            v=randint(1,9)
            if checkIfElementduplicates(board,v,i,j)=="No":
                board[i][j]=v

def sudokuSolution(board):
    for i in range(9):
        for j in range(9):
            v=randrange(1,10)
            while checkIfElementduplicates(board,v,i,j)!="No":
                v=randrange(1,10)
            board[i][j]=v
        displaySudoku(board)

def enterMove(board):
    row=int(input("Enter a row no from[0 to 8]:"))
    col=int(input("Enter a column no from[0 to 8]:"))
    val=int(input("Enter a value from[1 to 9] as per sudoku rule:"))
    if checkIfElementduplicates(board,val,row,col)=="Yes" :
        print("Value violating Sudoku rule try again:")
        enterMove(board)
    else :
        board[row][col]=val
        
def checkIfSudokuIsComplete(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] not in [1,2,3,4,5,6,7,8,9]:
                return "No"

    return "Yes"

#Execution of tasks start here
board=[[],[],[],[],[],[],[],[],[]] #Creating a blank list with 9 rows
for i in range(9):
    for j in range(9):
        board[i].append(" ") #Creating a 9*9 board with intial value as a space
        
#presetSudoku(board) #Preset some cells of sudoku board with random intial values
sudokuSolution(board)
displaySudoku(board)

"""
while True:
    if checkIfSudokuIsComplete(board)=="No":
        enterMove(board)
    else:
        print("Sudoku is completed Successfully!")
        break
"""

#displaySudoku(board)

sleep(10)
quit

