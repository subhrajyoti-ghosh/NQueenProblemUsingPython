import pprint

class NQueen:
    def __init__(self,N):
        self.N = N
        self.Board = []
        self.rowStack = []                                                               ##Row positions will be placed in this stack
        self.PlacedQueens = 0                                                            ##Number of placed Queens. Once all queens are placed, this will be 8 which is the breaking condition
    
    ##Below function will generate the board
    def generateBoard(self):
        #print("{}".format(self.Board))
        for i in range(self.N):
            tempBoard=[]
            for j in range(self.N):
                tempBoard.append(0)
                #print(tempBoard)
            self.Board.append(tempBoard)
        #pprint.pprint(self.Board)
        ##return Board

    ##Below function checks if the current Queen position is safe or not
    ##If there is any queen in the same column of this row or any queen in any of the left diagonal then this is not correct position, then return False
    ##If all the checking fails that meansk, the queen position is safe, then return True
    ##Note : As we are going from left to right position, only left side checking is sufficient, as ther will not be any queen at the right
    def isSafe(self,row, col):

        # Check for all rows of this column
        for i in range(row):
            #print("Other columns --> [{}-{}]".format(row,i))                   ##For debugging purpose
            if self.Board[i][col] == 1:
                return False

        # Check for all columns of this row
        for i in range(col):
            #print("Other columns --> [{}-{}]".format(row,i))                   ##For debugging purpose
            if self.Board[row][i] == 1:
                return False

        # Check diagonal above the cell
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            #print("Top Diagonal --> [{}-{}]".format(i,j))                      ##For debugging purpose
            if self.Board[i][j] == 1:
                return False

        # Check the diagonal below the cell
        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            #print("Bottom Diagonal --> [{}-{}]".format(i,j))                   ##For debugging purpose
            if self.Board[i][j] == 1:
                return False

        return True

    ##Put Queens on the board
    ##Logic:
    ##Start with column 0
    ##Iterate through all rows
    ##First put queen at board(row=0,column=0)
    ##  Then calculate all rows and columnsand try to solve rest of the cells
    ##  After checking all of the cells if we cannot place all N queens, again repeat the same process starting from column 1
    ##  This way iterate through all of the columns
    ##If after checking all rows and columns if we see all N columns are filled, that means it's a success
    ##Otherwise there might be issue
    def putQueens(self, col):
        global PlacedQueens
        
        #print(col)                                                             ##For debugging purpose
        if self.PlacedQueens == self.N:
            return True

        for i in range(self.N): #Iterate this row
            print("{}".format(i))                                               ##For debugging purpose
            if self.isSafe(i, col) == True:
                self.Board[i][col] = 1
                self.PlacedQueens = self.PlacedQueens + 1
                self.rowStack.append(i)
                print("{}-{}-{}".format(i,col,self.PlacedQueens))                    ##For debugging purpose

                if self.putQueens(col+1) == True:                               ##Go to next column of the same row
                    print("{}-{}".format(i,col))                                ##For debugging purpose
                    return True
                else:
                    row = self.rowStack.pop()                                   ##As the position is wrong this is removed from stack
                    self.Board[row][col] = 0                                    ##If the above checking for this row for all columns is false that means we cannot place the Queen in this place
                    self.PlacedQueens = self.PlacedQueens - 1
        return False

    def displayBoard(self):
        for i in range(self.N):
            rowSetup = ""
            for j in range(self.N):
                if self.Board[j][i] == 0:
                    rowSetup = rowSetup + " X "
                else:
                    rowSetup = rowSetup + " Q "
            print("{}".format(rowSetup.strip()))

nQueenSolution = NQueen(8)
nQueenSolution.generateBoard()                                                  ##Initialize the board

if nQueenSolution.putQueens(0) == False:
    print("Cannot solve")
    pprint.pprint(nQueenSolution.Board)
else:
    print("Success!!")
    nQueenSolution.displayBoard()                                               ##Using custom function to improve UI
    #pprint.pprint(nQueenSolution.Board)                                        ##pprint displays the board in a nice way if N>4. If N<=4, the display is not good
