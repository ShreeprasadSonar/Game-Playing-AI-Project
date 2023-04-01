import sys
from commonFunctions import commonFunctions

class MiniMaxOpeningImproved() :
    positionsEvaluated = 0
    minimaxEstimate = 0
    cf = commonFunctions()
    
    # This score is used by the minimax algorithm to determine the best possible move for a player to make.
    def StaticEstimation(self, brd) :  
        self.positionsEvaluated += 1  
        wbMillDifference = self.millCountDiff(brd)
        wbPotentialMillsDifference = self.potentialMillsDiff(brd)
        return (40* (brd.count('W') - brd.count('B'))) + (8*wbMillDifference) +  (5*(wbPotentialMillsDifference))
    
    def millCountDiff(self, brd):
        wMills, bMills = 0, 0
        mills = [[0,1,2], [0,3,6], [2,5,7], [2,12,21], [3,4,5], [5,11,18], [6,9,13], [7,10,15], [10,11,12], [13,14,15], [13,16,19], [14,17,20], [15,18,21], [16,17,18], [19,20,21]]
        for mill in  mills:
            if brd[mill[0]] == brd[mill[1]] == brd[mill[2]]:
                if brd[mill[0]] == 'W':
                    wMills += 1
                elif brd[mill[0]] == 'B':
                    bMills += 1
        return wMills - bMills
    
    def potentialMillsDiff(self, brd):
        wpMills = 0
        bpMills = 0
        # print("For board : " + ''.join(brd)+ " ##############################################")
        for i in range(len(brd)):
            if brd[i] == 'x':
                neighbours = self.cf.Neighbours(i)
                board = brd.copy()
                board[i] = 'W'
                if self.cf.CloseMill(i, board):
                    # print("Mill closes for position " + str(i) + " : " + ''.join(board))
                    wpMills +=3 # If possible mill is formed
                    for n in neighbours:
                        if board[n] == 'W' and not(self.cf.CloseMill(n, board)):
                            wpMills += 1 # When there are neighbouring white pieces which are not part of a mill to fill the position
                        elif board[n] == 'B':
                            wpMills -= 2 # When there are neighbouring black pieces to block the position
                board[i] = 'B'
                if self.cf.CloseMill(i, board):
                    bpMills +=3 
                    for n in neighbours:
                        if board[n] == 'B' and not(self.cf.CloseMill(n, board)):
                            bpMills += 1 # When there are neighbouring black pieces which are not part of a mill to fill the position
                        elif board[n] == 'W':
                            bpMills -= 2 # When there are neighbouring white pieces to block the position
        return wpMills - bpMills
    

    def MaxMin(self, brdPos, depth):
        if depth == 0:
            return brdPos
        # print("MaxMin Current Depth: " + str(depth) + " ##################################################################")
        depth -= 1
        # GenerateAdd Generates moves created by adding a white piece at x.
        i, v, wMoves, mnBrd, mxBrd = 0, float('-inf'), self.cf.GenerateAdd(brdPos), [], []
        # for wMove in wMoves : print("Possible Moves For White: " +  ''.join(wMove))
        # print("Possible Moves For White: " +  str(len(wMoves)))
        # For each child y (wMove) of x (wMoves)
        while (i < len(wMoves)) :
                # Tree for min
            mnBrd = self.MinMax(wMoves[i], depth)
            staticEs = self.StaticEstimation(mnBrd)
            if (v < staticEs) :
                v = staticEs
                self.minimaxEstimate = v
                mxBrd = wMoves[i]
            i += 1
        return mxBrd

    def MinMax(self, brdPos, depth) :
        if depth == 0:
            return brdPos
        # print("MinMax Current Depth: " + str(depth) + " ##################################################################")
        depth -= 1
        # GenerateBlackMoves Generates moves created by adding a black piece at x.
        i, v, bMoves, mxBrd, mnBrd =  0, float('inf'), self.cf.GenerateBlackMoves(brdPos), [], []
        # for bMove in bMoves : print("Possible Moves For Black: " +  ''.join(bMove))
        # print("Possible Moves For Black: " +  str(len(bMoves)))
        while (i < len(bMoves)) :
            # Tree for max
            mxBrd = self.MaxMin(bMoves[i], depth)
            staticEs = self.StaticEstimation(mxBrd)
            if (v > staticEs) :
                v = staticEs
                mnBrd = bMoves[i]
            i += 1
        return mnBrd 

if __name__=="__main__":
    try: 
        with open(sys.argv[1], 'r') as f:
            brd1 = f.read()
            brd1List = list(brd1)
        depth = int(sys.argv[3])
        if len(brd1) != 22:
            print("Invalid board1.txt length : ", len(brd1))
        
        mmoi = MiniMaxOpeningImproved()       
        movePlayedList = mmoi.MaxMin(brd1List, depth) # Invoke MaxMin
        movePlayed = ''.join(movePlayedList)
        
        print("\n## MiniMaxOpeningImproved.py ##\n")
        print("Given Board : " + brd1 + "\nGiven Depth : " + str(depth)+ "\n")
        
        print("Board Position: ", movePlayed)
        print("Positions evaluated by static estimation: ", mmoi.positionsEvaluated)
        print("MINIMAX estimate: ", mmoi.minimaxEstimate)
        
        print("\nInput Board:\n")
        mmoi.cf.printBoard(brd1)
        print("\nOutput Board:\n")
        mmoi.cf.printBoard(movePlayed)
        
        with open(sys.argv[2], 'w') as f:
            f.write(movePlayed)

    except:
        print("Please specify in format: Python MiniMaxOpeningImproved.py board1.txt board2.txt 2")