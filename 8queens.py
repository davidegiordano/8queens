class Chessboard:
    def __init__(self):
        #Create a matrix 8x8
        self.chessboard = [[0 for x in range(0, 8)] for y in range(0, 8)]

    def printChessboard(self):
        for x in self.chessboard:
            for y in x:
                #Print the current chessboard with a new line only in new row
                print("["+str(y)+"]", end='', flush=True)
            print()

    def isCellFree(self, x, y):
        if x < 0 or y < 0 or x >= 8 or y >= 8:
            return False
        return self.chessboard[x][y] == 0

    #Check if position x,y is valid to put another queen
    def isQueenSafe(self, x, y):

        if x >= 8 or x < 0 or y < 0 or y >= 8:
            return False
        
        for i in range(8):
            
            #Check rows
            #If there is another queen in the same row x,y is not a valid position
            if self.chessboard[x][i] != 0:
                return False

            #Check columns
            #If there is another queen in the same column x,y is not a valid position
            if self.chessboard[i][y] != 0:
                return False
            
            #Check diagonals
            #If there is another queen in any diagonal x,y is not a valid position
            
            #\
            # >
            if x+i < 8 and y+i < 8 and self.chessboard[x+i][y+i] != 0:
                return False

            # /
            #<
            if x+i < 8 and y-i >= 0 and self.chessboard[x+i][y-i] != 0:
                return False

            # >
            #/
            if x-i >= 0 and y+i < 8 and self.chessboard[x-i][y+i] != 0:
                return False

            #<
            # \
            if x-i >= 0 and y-i >= 0 and self.chessboard[x-i][y-i] != 0:
                return False

        
        return True

    #Insert a queen in chessboard at position x,y
    def putQueen(self, x, y):
        if x < 0 or y < 0:
            return False
        if self.isCellFree(x, y) and self.isQueenSafe(x, y):
            self.chessboard[x][y] = 1 #Put queen in x,y
        return True

    def clearChessboard(self):
        for i in range(8):
            for j in range(8):
                self.chessboard[i][j] = 0

#main
eightQueens = Chessboard()
print("Before")
eightQueens.printChessboard()
print()
print("After")

for i in range(8):
    for j in range(8):
        eightQueens.putQueen(i, j)

eightQueens.printChessboard()
