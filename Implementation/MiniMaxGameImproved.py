import sys
class MiniMaxGameImproved(object) :
    positionsEvaluated = 0
    minimaxEstimate = 0
    def GenerateMovesMidgameEndgame(self, brdPos) :
        return self.GenerateHopping(brdPos) if (brdPos.count('W') == 3) else self.GenerateMove(brdPos)

    # Generates moves created by white pieces hopping (to be used in the endgame).
    def GenerateHopping(self, brdPos) :
        brdPosHopList, i =  [], 0
        while (i < len(brdPos)) :
            if (brdPos[i] == 'W') :
                j = 0
                while (j < len(brdPos)) :
                    if (brdPos[j] == 'x') :
                        board = brdPos.copy()
                        board[i] = 'x'
                        board[j] = 'W'
                        if (self.CloseMill(j, board)) :
                            self.GenerateRemove(board, brdPosHopList)
                        else :
                            brdPosHopList.append(board)
                    j += 1
            i += 1
        return brdPosHopList
    
    # Generates moves created by moving a white piece to an adjacent location (to be used in the midgame).
    def GenerateMove(self, brdPos) :
        brdPosMoveList, i =  [], 0
        while (i < len(brdPos)) :
            if (brdPos[i] == 'W') :
                neighbourslist = self.Neighbours(i)
                for j in neighbourslist :
                    if (brdPos[j] == 'x') :
                        board = brdPos.copy()
                        board[i] = 'x'
                        board[j] = 'W'
                        if (self.CloseMill(j, board)) :
                            brdPosMoveList = self.GenerateRemove(board, brdPosMoveList)
                        else :
                            brdPosMoveList.append(board)
            i += 1
        return brdPosMoveList
    
    # Method of generating moves created (Positions), after removing a black piece from the board.
    def GenerateRemove(self, brd,  brdPosList) :
        moves, i = brdPosList.copy(), 0
        positionAppended = False
        while (i < len(brd)) :
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
    
    def GenerateBlackMoves(self, brdPos) :
        board, blackMoves, result = brdPos.copy(), [], []
        # Swap W and B so that moves can be evaluated for B from prespective of W
        board = self.Swap(board)
        blackMoves = self.GenerateMovesMidgameEndgame(board)
        for move in blackMoves :
            move = self.Swap(move)
            result.append(move)
        return result
    
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
                neighbours = self.Neighbours(i)
                board = brd.copy()
                board[i] = 'W'
                if self.CloseMill(i, board):
                    # print("Mill closes for position " + str(i) + " : " + ''.join(board))
                    wpMills +=3 # If possible mill is formed
                    for n in neighbours:
                        if board[n] == 'W' and not(self.CloseMill(n, board)):
                            wpMills += 1 # When there are neighbouring white pieces which are not part of a mill to fill the position
                        elif board[n] == 'B':
                            wpMills -= 2 # When there are neighbouring black pieces to block the position
                board[i] = 'B'
                if self.CloseMill(i, board):
                    bpMills +=3 
                    for n in neighbours:
                        if board[n] == 'B' and not(self.CloseMill(n, board)):
                            bpMills += 1 # When there are neighbouring black pieces which are not part of a mill to fill the position
                        elif board[n] == 'W':
                            bpMills -= 2 # When there are neighbouring white pieces to block the position
        return wpMills - bpMills
                
    
    def Swap(self, brd) :
        board = brd.copy()
        # Dictionary to map 'W' to 'B' and 'B' to 'W'
        swap_dict = {'W': 'B', 'B': 'W'}
        # Using a list comprehension to replace each character in the string with its swapped value
        swapped_brd = ''.join([swap_dict.get(char, char) for char in ''.join(board)])
        return list(swapped_brd)
    
        # Return neighbours of corresponding location
    def Neighbours(self, j) :
        if j==0 : return [1, 3, 19]
        elif j==1 : return [0, 2, 4]
        elif j==2 : return [1, 5, 12]
        elif j==3 : return [0, 4, 6, 8]
        elif j==4 : return [1, 3, 5]
        elif j==5 : return [2, 4, 7 ,11]
        elif j==6 : return [3, 7, 9]
        elif j==7 : return [5, 6, 10]
        elif j==8 : return [3, 9, 16]
        elif j==9 : return [6, 8, 13]
        elif j==10 : return [7, 11, 15] 
        elif j==11 : return [5, 10, 12, 18]
        elif j==12 : return [2, 11, 21]
        elif j==13 : return [9, 14, 16]
        elif j==14 : return [13, 15, 17]
        elif j==15 : return [10, 14, 18]
        elif j==16 : return [8, 13, 17, 19]
        elif j==17 : return [14, 16, 18, 20]
        elif j==18 : return [11, 15, 17, 21]
        elif j==19 : return [0, 16, 20]
        elif j==20 : return [17, 19, 21]
        elif j==21 : return [12, 18, 20] 
        else : print("Invalid Neighbour location")

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
        i, v, wMoves, mnBrd, mxBrd = 0, float('-inf'), self.GenerateMovesMidgameEndgame(brdPos), [], []
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
    
    def printBoard(self, board):
        print("{}-----------{}-----------{}".format(board[19], board[20], board[21]))
        print("| \         |         / |")
        print("|   {}-------{}-------{}   |".format(board[16], board[17], board[18]))
        print("|   | \     |     / |   |")
        print("|   |   {}---{}---{}   |   |".format(board[13], board[14], board[15]))
        print("|   |   |       |   |   |")
        print("|   {}---{}       {}---{}---{}".format(board[8], board[9], board[10], board[11], board[12]))
        print("|   |   |       |   |   |")
        print("|   |   {}-------{}   |   |".format(board[6], board[7]))
        print("|   | /           \ |   |")
        print("|   {}-------{}-------{}   |".format(board[3], board[4], board[5]))
        print("| /         |         \ |")
        print("{}-----------{}-----------{}".format(board[0], board[1], board[2]))
        print()


if __name__=="__main__":
    try: 
        with open(sys.argv[1], 'r') as f:
            brd1 = f.read()
            brd1List = list(brd1)
        depth = int(sys.argv[3])
        if len(brd1) != 22:
            print("Invalid board1.txt length : ", len(brd1))
        
        mmgi = MiniMaxGameImproved()       
        movePlayedList = mmgi.MaxMin(brd1List, depth) # Invoke MaxMin
        movePlayed = ''.join(movePlayedList)
        
        print("\n## MiniMaxGameImproved.py ##\n")
        print("Given Board : " + brd1 + "\nGiven Depth : " + str(depth)+ "\n")
        
        print("Board Position: ", movePlayed)
        print("Positions evaluated by static estimation: ", mmgi.positionsEvaluated)
        print("MINIMAX estimate: ", mmgi.minimaxEstimate)
        
        print("\nInput Board:\n")
        mmgi.printBoard(brd1)
        print("\nOutput Board:\n")
        mmgi.printBoard(movePlayed)
        
        with open(sys.argv[2], 'w') as f:
            f.write(movePlayed)

    except:
        print("Please specify in format: Python MiniMaxGameImproved.py board1.txt board2.txt 2")