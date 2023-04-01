import sys
from commonFunctions import commonFunctions

class MiniMaxGameBlack(object) :
    cf = commonFunctions()
    positionsEvaluated = 0
    minimaxEstimate = 0
    
    def StaticEstimation(self, brd) :
        self.positionsEvaluated += 1 
        whites, blacks = brd.count('W'), brd.count('B')
        numBlackMoves = len(self.cf.GenerateBlackMoves(brd))
        if (blacks <= 2) :
            return 10000
        elif(whites <= 2) :
            return -10000
        elif(numBlackMoves == 0) :
            return 10000
        else :
            return ((1000 * (whites - blacks)) - numBlackMoves)

    def MaxMin(self, brdPos, depth):
        if depth == 0:
            return brdPos
        depth -= 1
        # GenerateAdd Generates moves created by adding a white piece at x.
        i, v, wMoves, mnBrd, mxBrd = 0, float('-inf'), self.cf.GenerateMovesMidgameEndgame(brdPos), [], []
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
        depth -= 1
        # GenerateBlackMoves Generates moves created by adding a black piece at x.
        i, v, bMoves, mxBrd, mnBrd =  0, float('inf'), self.cf.GenerateBlackMoves(brdPos), [], []
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
        
        mmgb = MiniMaxGameBlack()    
        # Invoke MaxMin and play a game by first swaping board for prespective of black and swap back again   
        movePlayedList = mmgb.cf.Swap(mmgb.MaxMin(mmgb.cf.Swap(brd1List), depth)) # Invoke MaxMin
        movePlayed = ''.join(movePlayedList)
        
        print("Board Position: ", movePlayed)
        print("Positions evaluated by static estimation: ", mmgb.positionsEvaluated)
        print("MINIMAX estimate: ", mmgb.minimaxEstimate)
        
        with open(sys.argv[2], 'w') as f:
            f.write(movePlayed)

    except:
        print("Please specify in format: Python MiniMaxGameBlack.py board1.txt board2.txt 2")