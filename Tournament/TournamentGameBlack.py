import sys
from commonFunctions import commonFunctions
import time

class TournamentGame(object) :
    positionsEvaluated = 0
    minimaxEstimate = 0
    cf = commonFunctions()
    
    # This score is used by the minimax algorithm to determine the best possible move for a player to make.
    def StaticEstimation(self, brd) :  
        bonus = 0
        if brd.count('B') < 3:
            bonus = 10000
        elif brd.count('W') < 3:  
            bonus = -10000
        self.positionsEvaluated += 1  
        wbMillDifference = self.millCountDiff(brd)
        wbPotentialMillsDifference = self.potentialMillsDiff(brd)
        return (40* (brd.count('W') - brd.count('B'))) + (8*wbMillDifference) +  (5*(wbPotentialMillsDifference)) + bonus
    
    def millCountDiff(self, brd):
        wMills, bMills = 0, 0
        mills = [[0,1,2], [0,3,6], [2,5,7], [2,12,21], [3,4,5], [5,11,18], [6,9,13], [7,10,15], [10,11,12], [13,14,15], [13,16,19], [14,17,20], [15,18,21], [16,17,18], [19,20,21]]
        for mill in  mills:
            try:
                if brd[mill[0]] == brd[mill[1]] == brd[mill[2]]:
                    if brd[mill[0]] == 'W':
                        wMills += 1
                    elif brd[mill[0]] == 'B':
                        bMills += 1
            except:
                continue        
        return wMills - bMills
    
    def potentialMillsDiff(self, brd):
        wpMills = 0
        bpMills = 0
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
                            wpMills -= 3 # When there are neighbouring black pieces to block the position
                board[i] = 'B'
                if self.cf.CloseMill(i, board):
                    bpMills +=3 
                    for n in neighbours:
                        if board[n] == 'B' and not(self.cf.CloseMill(n, board)):
                            bpMills += 1 # When there are neighbouring black pieces which are not part of a mill to fill the position
                        elif board[n] == 'W':
                            bpMills -= 3 # When there are neighbouring white pieces to block the position
        return wpMills - bpMills

    def MaxMin(self, brdPos, depth, alpha, beta, startTime, timeLimit):
        if depth == 0:
            return brdPos
        depth -= 1
        # GenerateAdd Generates moves created by adding a white piece at x.
        i, v, wMoves, mnBrd, mxBrd = 0, float('-inf'), self.cf.GenerateMovesMidgameEndgame(brdPos), [], []
        while (i < len(wMoves)) :
            # Tree for min
            mnBrd = self.MinMax(wMoves[i], depth, alpha, beta, startTime, timeLimit)
            if mnBrd is None:
                return None
            staticEs = self.StaticEstimation(mnBrd)
            if (v < staticEs) :
                v = staticEs
                self.minimaxEstimate = v
                mxBrd = wMoves[i]
            if (v >= beta) : return mxBrd
            else : alpha = max(v, alpha)
            i += 1
        return mxBrd

    def MinMax(self, brdPos, depth, alpha, beta, startTime, timeLimit) :
        if (time.time() - startTime) > timeLimit:
            return None
        if depth == 0:
            return brdPos
        depth -= 1
        # GenerateBlackMoves Generates moves created by adding a black piece at x.
        i, v, bMoves, mxBrd, mnBrd =  0, float('inf'), self.cf.GenerateBlackMoves(brdPos), [], []
        while (i < len(bMoves)) :
            # Tree for max
            mxBrd = self.MaxMin(bMoves[i], depth, alpha, beta, startTime, timeLimit)
            if mxBrd is None:
                return None
            staticEs = self.StaticEstimation(mxBrd)
            if (v > staticEs) :
                v = staticEs
                mnBrd = bMoves[i]
            if (v <= alpha) : return mnBrd
            else: beta = min(v, beta)
            i += 1
        return mnBrd 


if __name__=="__main__":
    try: 
        with open(sys.argv[1], 'r') as f:
            brd1 = f.read()
            brd1List = list(brd1)
        depth = 0
        if len(brd1) != 22:
            print("Invalid board1.txt length : ", len(brd1))
        
        tg = TournamentGame()
        startTime = time.time()
        timeLimit = 5
        
        print("\nInput Board:\n")
        tg.cf.printBoard(brd1)
        
        for depth in range(1, 100):  
            alpha, beta = float('-inf'), float('inf')     
            movePlayedList = tg.MaxMin(tg.cf.Swap(brd1List), depth, alpha, beta, startTime, timeLimit) # Invoke MaxMin
            if movePlayedList is None:
                break
            movePlayed = ''.join(tg.cf.Swap(movePlayedList))
        
        print("\n## TournamentGame.py ##\n")
        print("Given Board : " + brd1 + "\nDepth Covered : " + str(depth)+ "\n")
        
        print("Move : ", movePlayed)
        # print("Positions evaluated by static estimation: ", tg.positionsEvaluated)
        # print("MINIMAX estimate: ", tg.minimaxEstimate)

        print("\nOutput Board:\n")
        tg.cf.printBoard(movePlayed)
        
        with open(sys.argv[2], 'w') as f:
            f.write(movePlayed)

    except:
        print("Please specify in format: Python TournamentGame.py board1.txt board2.txt")