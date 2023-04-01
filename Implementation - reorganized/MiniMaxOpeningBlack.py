import sys
from commonFunctions import commonFunctions

class MiniMaxOpeningBlack() :
    cf = commonFunctions()
    positionsEvaluated = 0
    minimaxEstimate = 0
    
    # This score is used by the minimax algorithm to determine the best possible move for a player to make.
    def StaticEstimation(self, brd) :  
        self.positionsEvaluated += 1  
        return brd.count('W') - brd.count('B')

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
                mxBrd = wMoves[i]
                self.minimaxEstimate = v
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
        
        mmob = MiniMaxOpeningBlack()    
        # Invoke MaxMin and play a game by first swaping board for prespective of black and swap back again
        movePlayedList = mmob.cf.Swap(mmob.MaxMin(mmob.cf.Swap(brd1List), depth)) 
        movePlayed = ''.join(movePlayedList)
        
        print("\n## MiniMaxOpeningBlack.py ##\n")
        print("Given Board : " + brd1 + "\nGiven Depth : " + str(depth)+ "\n")
        
        print("Board Position: ", movePlayed)
        print("Positions evaluated by static estimation: ", mmob.positionsEvaluated)
        print("MINIMAX estimate: ", mmob.minimaxEstimate)

        
        print("\nInput Board:\n")
        mmob.cf.printBoard(brd1)
        print("\nOutput Board:\n")
        mmob.cf.printBoard(movePlayed)
        
        with open(sys.argv[2], 'w') as f:
            f.write(movePlayed)

    except:
        print("Please specify in format: Python MiniMaxOpeningBlack.py board1.txt board2.txt 2")