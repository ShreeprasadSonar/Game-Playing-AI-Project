import sys
class MiniMaxOpening() :
    positionsEvaluated = 0
    minimaxEstimate = 0
    
    # Generates moves created by adding a white piece (to be used in the opening).
    def GenerateAdd(self, brdPos) :
        brdPosList, i =  [], 0
        while (i < len(brdPos)) :
            if (brdPos[i] == 'x') :
                board = brdPos.copy()
                board[i] = 'W'
                if (self.CloseMill(i, board)) :
                    # GenerateRemove fuction adds the moves to the list and returns it
                    brdPosList = self.GenerateRemove(board, brdPosList)
                else :
                    brdPosList.append(board)
            i += 1
        return brdPosList
    
    # Method of generating moves created (Positions), after removing a black piece from the board.
    def GenerateRemove(self, brd,  brdPosList):
        moves, i = brdPosList.copy(), 0
        while (i < len(brd)) :
            positionAppended = False
            if (brd[i] == 'B') :
                if (not(self.CloseMill(i, brd))) :
                    # print("In Black does not have a mill : ", brd)
                    board = brd.copy()
                    board[i] = 'x'
                    positionAppended = True
                    moves.append(board)
            i += 1
        if positionAppended == False:
            board = brd.copy()
            moves.append(board)
        return moves # positions are added to L by removing black pieces
    
    # This score is used by the minimax algorithm to determine the best possible move for a player to make.
    def StaticEstimation(self, brd) :  
        self.positionsEvaluated += 1  
        return brd.count('W') - brd.count('B')
    
    def Swap(self, x) :
        brd = x.copy()
        # Create a dictionary to map 'W' to 'B' and 'B' to 'W'
        swap_dict = {'W': 'B', 'B': 'W'}
        # Use a list comprehension to replace each character in the string with its swapped value
        swapped_brd = ''.join([swap_dict.get(char, char) for char in ''.join(brd)])
        return list(swapped_brd)

    def GenerateBlackMoves(self, brdPos) :
        board, blackMoves, result = brdPos.copy(), [], []
        # Swap W and B so that moves can be evaluated for B from prespective of W
        board = self.Swap(board)
        blackMoves = self.GenerateAdd(board)
        for move in blackMoves :
            move = self.Swap(move)
            result.append(move)
        return result
    
    # If move to loc closes a mill return true
    def CloseMill(self, loc, board) :
        c = board[loc]
        if (c == 'W' or c == 'B') :
            if loc==0 :
                return True if ((board[3] == c and board[6] == c) or (board[1] == c and board[2] == c)) else False              
            elif loc==1 :
                return True if (board[0] == c and board[2] == c) else False
            elif loc==2 :
                return True if ((board[0] == c and board[1] == c) or (board[5] == c and board[7] == c) or (board[12] == c and board[21] == c)) else False
            elif loc==3 :
                return True if ((board[8] == c and board[16] == c) or (board[0] == c and board[6] == c) or (board[4] == c and board[5] == c)) else False
            elif loc==4 :
                return True if (board[3] == c and board[5] == c) else False
            elif loc==5 :
                return True if ((board[3] == c and board[4] == c) or (board[2] == c and board[7] == c) or (board[11] == c and board[18] == c)) else False
            elif loc==6 :
                return True if ((board[0] == c and board[3] == c) or (board[9] == c and board[13] == c)) else False
            elif loc==7 :
                return True if ((board[10] == c and board[15] == c) or (board[2] == c and board[5] == c)) else False
            elif loc==8 :
                return True if (board[3] == c and board[16] == c) else False
            elif loc==9 :
                return True if (board[6] == c and board[13] == c) else False
            elif loc==10 :
                return True if ((board[7] == c and board[15] == c) or (board[11] == c and board[12] == c)) else False
            elif loc==11 :
                return True if ((board[10] == c and board[12] == c) or (board[5] == c and board[18] == c)) else False
            elif loc==12 :
                return True if ((board[10] == c and board[11] == c) or (board[2] == c and board[21] == c)) else False
            elif loc==13 :
                return True if ((board[16] == c and board[19] == c) or (board[14] == c and board[15] == c) or (board[9] == c and board[6] == c)) else False
            elif loc==14 :
                return True if ((board[13] == c and board[15] == c) or (board[17] == c and board[20] == c)) else False
            elif loc==15 :
                return True if ((board[13] == c and board[14] == c) or (board[18] == c and board[21] == c) or (board[7] == c and board[10] == c)) else False
            elif loc==16 :
                return True if ((board[13] == c and board[19] == c) or (board[17] == c and board[18] == c) or (board[3] == c and board[8] == c)) else False
            elif loc==17 :
                return True if ((board[16] == c and board[18] == c) or (board[14] == c and board[20] == c)) else False
            elif loc==18 :
                return True if ((board[16] == c and board[17] == c) or (board[15] == c and board[21] == c) or (board[5] == c and board[11] == c)) else False
            elif loc==19 :
                return True if ((board[20] == c and board[21] == c) or (board[13] == c and board[16] == c)) else False
            elif loc==20 :
                return True if ((board[19] == c and board[21] == c) or (board[14] == c and board[17] == c)) else False
            elif loc==21 :
                return True if ((board[19] == c and board[20] == c) or (board[15] == c and board[18] == c) or (board[2] == c and board[12] == c)) else False
        return False

    def MaxMin(self, brdPos, depth):
        if depth == 0:
            return brdPos
        # print("MaxMin Current Depth: " + str(depth) + " ##################################################################")
        depth -= 1
        # GenerateAdd Generates moves created by adding a white piece at x.
        i, v, wMoves, mnBrd, mxBrd = 0, float('-inf'), self.GenerateAdd(brdPos), [], []
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
        i, v, bMoves, mxBrd, mnBrd =  0, float('inf'), self.GenerateBlackMoves(brdPos), [], []
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