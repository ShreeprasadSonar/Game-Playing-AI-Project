import sys
class MiniMaxOpening() :
    positionsEvaluated = 0
    minimaxEstimate = 0
    
    # Generates moves created by adding a white piece (to be used in the opening).
    def GenerateAdd(self, brdPos) :
        brdPosList =  []
        brdCopy = None
        i = 0
        while (i < len(brdPos)) :
            if (brdPos[i] == 'x') :
                brdCopy = brdPos.copy()
                brdCopy[i] = 'W'
                if (self.CloseMill(i, brdCopy)) :
                    # GenerateRemove fuction adds the moves to the list and returns it
                    brdPosList = self.GenerateRemove(brdCopy, brdPosList)
                else :
                    brdPosList.append(brdCopy)
            i += 1
        return brdPosList
    
    # Method of generating moves created (Positions), after removing a black piece from the board.
    def GenerateRemove(self, brd,  brdPosList) :
        list = brdPosList.copy()
        i = 0
        while (i < len(brd)) :
            if (brd[i] == 'B') :
                if (not (self.CloseMill(i, brd))) :
                    # print("In Black does not have a mill : ", brd)
                    brdCopy = brd.copy()
                    brdCopy[i] = 'x'
                    list.append(brdCopy)
                else :
                    # print("In Black has a mill")
                    brdCopy = brd.copy()
                    list.append(brdCopy)
            i += 1
        return list # positions are added to L by removing black pieces
    
    # This score is used by the minimax algorithm to determine the best possible move for a player to make.
    def StaticEstimation(self, brd) :    
        return brd.count('W') - brd.count('B')
    
    def Swap(self, x) :
        brd = x.copy()
        # Create a dictionary to map 'W' to 'B' and 'B' to 'W'
        swap_dict = {'W': 'B', 'B': 'W'}
        # Use a list comprehension to replace each character in the string with its swapped value
        swapped_brd = ''.join([swap_dict.get(char, char) for char in ''.join(brd)])
        return list(swapped_brd)

    def GenerateBlackMoves(self, brdPos) :
        brdCopy = brdPos.copy()
        generatedBlackMoves =  []
        generatedBlackMovesActualOutcome =  []
        # Swap W and B so that moves can be evaluated for B from prespective of W
        brdCopy = self.Swap(brdCopy)
        generatedBlackMoves = self.GenerateAdd(brdCopy)
        for move in generatedBlackMoves :
            move = self.Swap(move)
            generatedBlackMovesActualOutcome.append(move)
        return generatedBlackMovesActualOutcome
    
        # If move to j closes a mill return true
    def CloseMill(self, loc,  brdCopy) :
        c = brdCopy[loc]
        if (c == 'W' or c == 'B') :
            if loc==0 :
                if ((brdCopy[3] == c and brdCopy[6] == c) or (brdCopy[1] == c and brdCopy[2] == c)) :
                    return True
                else : return False               
            elif loc==1 :
                if (brdCopy[0] == c and brdCopy[2] == c) :
                    return True
                else : return False
            elif loc==2 :
                if ((brdCopy[0] == c and brdCopy[1] == c) or (brdCopy[5] == c and brdCopy[7] == c) or (brdCopy[12] == c and brdCopy[21] == c)) :
                    return True
                else : return False
            elif loc==3 :
                if ((brdCopy[8] == c and brdCopy[16] == c) or (brdCopy[0] == c and brdCopy[6] == c) or (brdCopy[4] == c and brdCopy[5] == c)) :
                    return True
                else : return False
            elif loc==4 :
                if (brdCopy[3] == c and brdCopy[5] == c) :
                    return True
                else : return False
            elif loc==5 :
                if ((brdCopy[3] == c and brdCopy[4] == c) or (brdCopy[2] == c and brdCopy[7] == c) or (brdCopy[11] == c and brdCopy[18] == c)) :
                    return True
                else : return False
            elif loc==6 :
                if ((brdCopy[0] == c and brdCopy[3] == c) or (brdCopy[9] == c and brdCopy[13] == c)) :
                    return True
                else : return False
            elif loc==7 :
                if ((brdCopy[10] == c and brdCopy[15] == c) or (brdCopy[2] == c and brdCopy[5] == c)) :
                    return True
                else : return False
            elif loc==8 :
                if (brdCopy[3] == c and brdCopy[16] == c) :
                    return True
                else : return False
            elif loc==9 :
                if (brdCopy[6] == c and brdCopy[13] == c) :
                    return True
                else : return False
            elif loc==10 :
                if ((brdCopy[7] == c and brdCopy[15] == c) or (brdCopy[11] == c and brdCopy[12] == c)) :
                    return True
                else : return False
            elif loc==11 :
                if ((brdCopy[10] == c and brdCopy[12] == c) or (brdCopy[5] == c and brdCopy[18] == c)) :
                    return True
                else : return False
            elif loc==12 :
                if ((brdCopy[10] == c and brdCopy[11] == c) or (brdCopy[2] == c and brdCopy[21] == c)) :
                    return True
                else : return False
            elif loc==13 :
                if ((brdCopy[16] == c and brdCopy[19] == c) or (brdCopy[14] == c and brdCopy[15] == c) or (brdCopy[9] == c and brdCopy[6] == c)) :
                    return True
                else : return False
            elif loc==14 :
                if ((brdCopy[13] == c and brdCopy[15] == c) or (brdCopy[17] == c and brdCopy[20] == c)) :
                    return True
                else : return False
            elif loc==15 :
                if ((brdCopy[13] == c and brdCopy[14] == c) or (brdCopy[18] == c and brdCopy[21] == c) or (brdCopy[7] == c and brdCopy[10] == c)) :
                    return True
                else : return False
            elif loc==16 :
                if ((brdCopy[13] == c and brdCopy[19] == c) or (brdCopy[17] == c and brdCopy[18] == c) or (brdCopy[3] == c and brdCopy[8] == c)) :
                    return True
                else : return False
            elif loc==17 :
                if ((brdCopy[16] == c and brdCopy[18] == c) or (brdCopy[14] == c and brdCopy[20] == c)) :
                    return True
                else : return False
            elif loc==18 :
                if ((brdCopy[16] == c and brdCopy[17] == c) or (brdCopy[15] == c and brdCopy[21] == c) or (brdCopy[5] == c and brdCopy[11] == c)) :
                    return True
                else : return False
            elif loc==19 :
                if ((brdCopy[20] == c and brdCopy[21] == c) or (brdCopy[13] == c and brdCopy[16] == c)) :
                    return True
                else : return False
            elif loc==20 :
                if ((brdCopy[19] == c and brdCopy[21] == c) or (brdCopy[14] == c and brdCopy[17] == c)) :
                    return True
                else : return False
            elif loc==21 :
                if ((brdCopy[19] == c and brdCopy[20] == c) or (brdCopy[15] == c and brdCopy[18] == c) or (brdCopy[2] == c and brdCopy[12] == c)) :
                    return True
                else : return False
        return False
    
    def MaxMin(self, brdPos,  depth) :
        if (depth > 0) :
            print("Current Depth at MaxMin: " + str(depth) + " ##################################################################")
            depth -= 1
            wMoves, mnBrd, mxBrd =  [], [], []
            v = float('-inf')
            # Generates moves created by adding a white piece at x.
            wMoves = self.GenerateAdd(brdPos)
            for wMove in wMoves :
                print("Possible moves for white: " +  ''.join(wMove))
            i = 0
            # For each child y (wMove) of x (wMoves)
            while (i < len(wMoves)) :
                # Tree for min
                mnBrd = self.MinMax(wMoves[i], depth)
                if (v < self.StaticEstimation(mnBrd)) :
                    v = self.StaticEstimation(mnBrd)
                    MiniMaxOpening.minimaxEstimate = v
                    mxBrd = wMoves[i]
                i += 1
            return mxBrd
        elif(depth == 0) :
            MiniMaxOpening.positionsEvaluated += 1
        return brdPos
    
    def MinMax(self, brdPos,  depth) :
        if (depth > 0) :
            print("current depth at MinMax is: " + str(depth) + " ##################################################################")
            depth -= 1
            bMoves, mxBrd, mnBrd =  [], [], []
            v = float('inf')
            # Generates moves created by adding a black piece at x.
            bMoves = self.GenerateBlackMoves(brdPos)
            for bMove in bMoves :
                print("the possible moves for black are: " +  ''.join(bMove))
            i = 0
            while (i < len(bMoves)) :
                # Tree for max
                mxBrd = self.MaxMin(bMoves[i], depth)
                if (v > self.StaticEstimation(mxBrd)) :
                    v = self.StaticEstimation(mxBrd)
                    mnBrd = bMoves[i]
                i += 1
            return mnBrd
        elif(depth == 0) :
            MiniMaxOpening.positionsEvaluated += 1
        return brdPos
    

if __name__=="__main__":
    try: 
        with open(sys.argv[1], 'r') as f:
            brd1 = f.read()
            brd1List = list(brd1)
        depth = int(sys.argv[3])
        if len(brd1) != 22:
            print("Invalid board1.txt length : ", len(brd1))
        print("Given Board : " + brd1 + "\nGiven Depth : " + str(depth))
        
        mmo = MiniMaxOpening()       
        movePlayedList = mmo.MaxMin(brd1List, depth) # Invoke MaxMin
        movePlayed = ''.join(movePlayedList)
        print("Board Position: ", movePlayed)
        print("Positions evaluated by static estimation: ", mmo.positionsEvaluated)
        print("MINIMAX estimate: ", mmo.minimaxEstimate)
        with open(sys.argv[2], 'w') as f:
            f.write(movePlayed)

    except:
        print("Please specify in format: Python MiniMaxOpening.py board1.txt board2.txt 2")