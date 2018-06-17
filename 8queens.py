import sys

class Chessboard:
    def __init__(self):
        #Create a matrix 8x8
        self.chessboard = [[0 for x in range(0, 8)] for y in range(0, 8)]

        #I try to break the lock with 8 queens in the first row, then
        #I move one by one all queens
        for y in range(8):
            self.chessboard[0][y] = 1

    def printChessboard(self):
        for x in self.chessboard:
            for y in x:
                #Print the current chessboard with a new line only in new row
                print("["+str(y)+"]", end='', flush=True)
            print()

    def isCellFree(self, x, y):
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False
        return self.chessboard[x][y] == 0

    #Check if position x,y is valid to put another queen
    def isQueenSafe(self, x, y):

        if x > 7 or x < 0 or y < 0 or y > 7:
            return False
        
        for i in range(8):
            
            #Check rows
            #If there is another queen in the same row x,y is not a valid position
            if i != y and self.chessboard[x][i] != 0:
                return False

            #Check columns
            #If there is another queen in the same column x,y is not a valid position
            if i != x and self.chessboard[i][y] != 0:
                return False
            
            #Check diagonals
            #If there is another queen in any diagonal x,y is not a valid position
            
            #\
            # >
            if i != 0 and x+i < 8 and y+i < 8 and self.chessboard[x+i][y+i] != 0:
                return False

            # /
            #<
            if i != 0 and x+i < 8 and y-i >= 0 and self.chessboard[x+i][y-i] != 0:
                return False

            # >
            #/
            if i != 0 and x-i >= 0 and y+i < 8 and self.chessboard[x-i][y+i] != 0:
                return False

            #<
            # \
            if i != 0 and x-i >= 0 and y-i >= 0 and self.chessboard[x-i][y-i] != 0:
                return False
        
        return True

    #Insert a queen in chessboard at position x,y
    def putQueen(self, x, y):
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False
        if self.isCellFree(x, y) and self.isQueenSafe(x, y):
            self.chessboard[x][y] = 1 #Put queen in x,y
            return True
        return False

    def clearChessboard(self):
        for i in range(8):
            for j in range(8):
                self.chessboard[i][j] = 0
        
        #Restart with the first row full of queen
        for x in range(8):
            self.chessboard[0][y] = 1

    #Not used, for future release
    def findMostLeftQueen(self):
        for x in range(8):
            for y in range(8):
                if self.chessboard[x][y] != 0:
                    return x, y
        return None, None

    def countQueens(self):
        count = 0
        
        for x in range(8):
            for y in range(8):
                if self.chessboard[x][y] != 0:
                    count += 1
        return count

    def validateAllQueensPositions(self):
        queensSafe = 0

        #Check all queens position
        for i in range(8):
            for j in range(8):
                if self.chessboard[i][j] != 0:
                    if self.isQueenSafe(i, j):
                        queensSafe += 1
                        
        if queensSafe != self.countQueens():
            return False
        return True

    def getRowByColumn(self, y):
        if y < 0 or y > 7:
            return None

        for i in range(8):
            if self.chessboard[i][y] != 0:
                return i
    
    def moveQueenAtColumn(self, y):
        x = self.getRowByColumn(y)

        if x is None or y < 0 or y > 7:
            return False

        #Move queen
        self.chessboard[x][y] = 0
        if x + 1 < 8:
            self.chessboard[x + 1][y] = 1
        else:
            self.chessboard[0][y] = 1
            
            #Prevents to move queens forever
            if y + 1 == 8:
                sys.exit(0)
            #Move the queen in the next column
            self.moveQueenAtColumn(y + 1)
            return True
        

    def foundSolution(self):
        while not self.validateAllQueensPositions():
            self.moveQueenAtColumn(0)
        print("Found a solution")
        self.printChessboard()
        print()
    
#main
eightQueens = Chessboard()
print("Before")
eightQueens.printChessboard()
print()
print("After")

#This may find the same solutions
for i in range(92):
    print("Solution " + str(i))
    eightQueens.foundSolution()
    eightQueens.moveQueenAtColumn(0)

