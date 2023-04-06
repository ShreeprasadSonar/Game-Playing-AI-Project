import sys
from commonFunctions import commonFunctions

class ABOpening() :
    positionsEvaluated = 0
    minimaxEstimate = 0
    cf = commonFunctions()
    
    # This score is used by the minimax algorithm to determine the best possible move for a player to make.
    def StaticEstimation(self, brd) :  
        self.positionsEvaluated += 1  
        return brd.count('W') - brd.count('B')

    def MaxMin(self, brdPos, depth, alpha, beta):
        if depth == 0:
            return brdPos
        depth -= 1
        # GenerateAdd Generates moves created by adding a white piece at x.
        i, v, wMoves, mnBrd, mxBrd = 0, float('-inf'), self.cf.GenerateAdd(brdPos), [], []
        while (i < len(wMoves)) :
            # Tree for min
            mnBrd = self.MinMax(wMoves[i], depth, alpha, beta)
            staticEs = self.StaticEstimation(mnBrd)
            if (v < staticEs) :
                v = staticEs
                self.minimaxEstimate = v
                mxBrd = wMoves[i]
            if (v >= beta) : return mxBrd
            else : alpha = max(v, alpha)
            i += 1
        return mxBrd

    def MinMax(self, brdPos, depth, alpha, beta) :
        if depth == 0:
            return brdPos
        depth -= 1
        # GenerateBlackMoves Generates moves created by adding a black piece at x.
        i, v, bMoves, mxBrd, mnBrd =  0, float('inf'), self.cf.GenerateBlackMovesOpening(brdPos), [], []
        while (i < len(bMoves)) :
            # Tree for max
            mxBrd = self.MaxMin(bMoves[i], depth, alpha, beta)
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
        depth = int(sys.argv[3])
        if len(brd1) != 22:
            print("Invalid board1.txt length : ", len(brd1))
        
        abo = ABOpening()       
        alpha, beta = float('-inf'), float('inf')
        movePlayedList = abo.MaxMin(brd1List, depth, alpha, beta) # Invoke MaxMin
        movePlayed = ''.join(movePlayedList)
        
        print("Board Position: ", movePlayed)
        print("Positions evaluated by static estimation: ", abo.positionsEvaluated)
        print("MINIMAX estimate: ", abo.minimaxEstimate)
        
        
        with open(sys.argv[2], 'w') as f:
            f.write(movePlayed)

    except:
        print("Please specify in format: Python ABOpening.py board1.txt board2.txt 2")