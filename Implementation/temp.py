# Java to Python by kalkicode.com
import sys
class MiniMaxGame(object) :
    positions_evaluated = 0
    minimax_estimate = 0
    def  generateMovesMidgameEndgame(self, x) :
        gmmeList =  []
        wcount = 0
        i = 0
        while (i < len(x)) :
            if (x[i] == 'W') :
                wcount += 1
            i += 1
        if (wcount == 3) :
            gmmeList = self.generateHopping(x)
            return gmmeList
        else :
            gmmeList = self.generateMove(x)
            return gmmeList
    def  generateHopping(self, x) :
        ghList =  []
        copyBoard = None
        i = 0
        while (i < len(x)) :
            if (x[i] == 'W') :
                j = 0
                while (j < len(x)) :
                    if (x[j] == 'x') :
                        copyBoard = x.clone()
                        copyBoard[i] = 'x'
                        copyBoard[j] = 'W'
                        if (self.closeMill(j, copyBoard)) :
                            self.generateRemove(copyBoard, ghList)
                        else :
                            ghList.append(copyBoard)
                    j += 1
            i += 1
        return ghList
    def  generateMove(self, x) :
        gmList =  []
        copyBoard = None
        nlist = None
        i = 0
        while (i < len(x)) :
            if (x[i] == 'W') :
                nlist = self.neighbours(i)
                for j in nlist :
                    if (x[j] == 'x') :
                        copyBoard = x.clone()
                        copyBoard[i] = 'x'
                        copyBoard[j] = 'W'
                        if (self.closeMill(j, copyBoard)) :
                            self.generateRemove(copyBoard, gmList)
                        else :
                            gmList.append(copyBoard)
            i += 1
        return gmList
    def  generateRemove(self, b,  list) :
        grList = ArrayList(list.clone())
        i = 0
        while (i < len(b)) :
            if (b[i] == 'B') :
                if (not (self.closeMill(i, b))) :
                    cbo = b.clone()
                    cbo[i] = 'x'
                    grList.append(cbo)
                else :
                    cbo = b.clone()
                    grList.append(cbo)
            i += 1
        return grList
    def  neighbours(self, j) :
        adj = [0] * (5)
        if j==0 :
           adj = [1, 2, 6]
           return adj
        elif j==1 :
           adj = [0, 11]
           return adj
        elif j==2 :
           adj = [0, 3, 4, 7]
           return adj
        elif j==3 :
           adj = [2, 10]
           return adj
        elif j==4 :
           adj = [2, 5, 8]
            return adj
        elif j==5 :
           adj = [4, 9]
            return adj
        elif j==6 :
           adj = [0, 7, 18]
            return adj
        elif j==7 :
           adj = [2, 6, 8, 15]
            return adj
        elif j==8 :
           adj = [4, 7, 12]
            return adj
        elif j==9 :
           adj = [5, 10, 14]
            return adj
        elif j==10 :
           adj = [3, 9, 11, 17]
            return adj
        elif j==11 :
           adj = [1, 10, 20]
            return adj
        elif j==12 :
           adj = [8, 13]
            return adj
        elif j==13 :
           adj = [12, 14, 16]
            return adj
        elif j==14 :
           adj = [9, 13]
            return adj
        elif j==15 :
           adj = [7, 16]
            return adj
        elif j==16 :
           adj = [13, 15, 17, 19]
            return adj
        elif j==17 :
           adj = [10, 16]
            return adj
        elif j==18 :
           adj = [6, 19]
            return adj
        elif j==19 :
           adj = [16, 18, 20]
            return adj
        elif j==20 :
           adj = [11, 19]
            return adj
        elif True :
           adj = None
            return adj
    def  closeMill(self, loc,  copyBoard) :
        c = copyBoard[loc]
        if (c == 'W' or c == 'B') :
            if loc==0 :
               if ((copyBoard[6] == c and copyBoard[18] == c) or (copyBoard[2] == c and copyBoard[4] == c)) :
                    return True
                else :
                    return False
            elif loc==6 :
               if ((copyBoard[7] == c and copyBoard[8] == c) or (copyBoard[0] == c and copyBoard[18] == c)) :
                    return True
                else :
                    return False
            elif loc==18 :
               if ((copyBoard[0] == c and copyBoard[6] == c) or (copyBoard[19] == c and copyBoard[20] == c)) :
                    return True
                else :
                    return False
            elif loc==2 :
               if ((copyBoard[0] == c and copyBoard[4] == c) or (copyBoard[7] == c and copyBoard[15] == c)) :
                    return True
                else :
                    return False
            elif loc==7 :
               if ((copyBoard[6] == c and copyBoard[8] == c) or (copyBoard[2] == c and copyBoard[15] == c)) :
                    return True
                else :
                    return False
            elif loc==15 :
               if ((copyBoard[7] == c and copyBoard[2] == c) or (copyBoard[16] == c and copyBoard[17] == c)) :
                    return True
                else :
                    return False
            elif loc==4 :
               if ((copyBoard[0] == c and copyBoard[2] == c) or (copyBoard[8] == c and copyBoard[12] == c)) :
                    return True
                else :
                    return False
            elif loc==8 :
               if ((copyBoard[6] == c and copyBoard[7] == c) or (copyBoard[4] == c and copyBoard[12] == c)) :
                    return True
                else :
                    return False
            elif loc==12 :
               if ((copyBoard[4] == c and copyBoard[8] == c) or (copyBoard[13] == c and copyBoard[14] == c)) :
                    return True
                else :
                    return False
            elif loc==13 :
               if ((copyBoard[12] == c and copyBoard[14] == c) or (copyBoard[16] == c and copyBoard[19] == c)) :
                    return True
                else :
                    return False
            elif loc==16 :
               if ((copyBoard[13] == c and copyBoard[19] == c) or (copyBoard[15] == c and copyBoard[17] == c)) :
                    return True
                else :
                    return False
            elif loc==19 :
               if ((copyBoard[13] == c and copyBoard[16] == c) or (copyBoard[18] == c and copyBoard[20] == c)) :
                    return True
                else :
                    return False
            elif loc==5 :
               if (copyBoard[9] == c and copyBoard[14] == c) :
                    return True
                else :
                    return False
            elif loc==9 :
               if ((copyBoard[5] == c and copyBoard[14] == c) or (copyBoard[10] == c and copyBoard[11] == c)) :
                    return True
                else :
                    return False
            elif loc==14 :
               if ((copyBoard[5] == c and copyBoard[9] == c) or (copyBoard[12] == c and copyBoard[13] == c)) :
                    return True
                else :
                    return False
            elif loc==3 :
               if (copyBoard[10] == c and copyBoard[17] == c) :
                    return True
                else :
                    return False
            elif loc==10 :
               if ((copyBoard[3] == c and copyBoard[17] == c) or (copyBoard[9] == c and copyBoard[11] == c)) :
                    return True
                else :
                    return False
            elif loc==17 :
               if ((copyBoard[3] == c and copyBoard[10] == c) or (copyBoard[15] == c and copyBoard[16] == c)) :
                    return True
                else :
                    return False
            elif loc==1 :
               if (copyBoard[11] == c and copyBoard[20] == c) :
                    return True
                else :
                    return False
            elif loc==11 :
               if ((copyBoard[1] == c and copyBoard[20] == c) or (copyBoard[9] == c and copyBoard[10] == c)) :
                    return True
                else :
                    return False
            elif loc==20 :
               if ((copyBoard[1] == c and copyBoard[11] == c) or (copyBoard[18] == c and copyBoard[19] == c)) :
                    return True
                else :
                    return False
        return False
    def  generateBlackMoves(self, x) :
        lboard = x.clone()
        i = 0
        while (i < len(lboard)) :
            if (lboard[i] == 'W') :
                lboard[i] = 'B'
                continue
            if (lboard[i] == 'B') :
                lboard[i] = 'W'
            i += 1
        gbm =  []
        gbmswap =  []
        gbm = self.generateMovesMidgameEndgame(lboard)
        for y in gbm :
            lsboard = y
            i = 0
            while (i < len(lsboard)) :
                if (lsboard[i] == 'W') :
                    lsboard[i] = 'B'
                    continue
                if (lsboard[i] == 'B') :
                    lsboard[i] = 'W'
                i += 1
            gbmswap.append(y)
        return gbmswap
    def  staticEstimation(self, sboard) :
        wcount = 0
        bcount = 0
        nbmList =  []
        nbmList = self.generateBlackMoves(sboard)
        bmovecount = len(nbmList)
        i = 0
        while (i < len(sboard)) :
            if (sboard[i] == 'W') :
                wcount += 1
            elif(sboard[i] == 'B') :
                bcount += 1
            i += 1
        if (bcount <= 2) :
            return 10000
        elif(wcount <= 2) :
            return -10000
        elif(bmovecount == 0) :
            return 10000
        else :
            return ((1000 * (wcount - bcount)) - bmovecount)
    def  MaxMin(self, x,  depth) :
        if (depth > 0) :
            print("current depth at MaxMin is" + str(depth))
            depth -= 1
            children =  []
            minBoard = None
            maxBoardchoice = [' '] * (50)
            children = self.generateMovesMidgameEndgame(x)
            for c in children :
                print("the possible moves for white are: " +  ''.join(c))
            v = -999999
            i = 0
            while (i < len(children)) :
                minBoard = self.MinMax(children[i], depth)
                if (v < self.staticEstimation(minBoard)) :
                    v = self.staticEstimation(minBoard)
                    MiniMaxGame.minimax_estimate = v
                    maxBoardchoice = children[i]
                i += 1
            return maxBoardchoice
        elif(depth == 0) :
            MiniMaxGame.positions_evaluated += 1
        return x
    def  MinMax(self, x,  depth) :
        if (depth > 0) :
            print("current depth at MinMax is" + str(depth))
            depth -= 1
            bchildren =  []
            maxBoard = None
            minBoardchoice = [' '] * (50)
            bchildren = self.generateBlackMoves(x)
            for bc in bchildren :
                print("the possible moves for black are: " +  ''.join(bc))
            v = 999999
            i = 0
            while (i < len(bchildren)) :
                maxBoard = self.MaxMin(bchildren[i], depth)
                if (v > self.staticEstimation(maxBoard)) :
                    v = self.staticEstimation(maxBoard)
                    minBoardchoice = bchildren[i]
                i += 1
            return minBoardchoice
        elif(depth == 0) :
            MiniMaxGame.positions_evaluated += 1
        return x
    def  swapWB(self, x) :
        lboard = x.clone()
        i = 0
        while (i < len(lboard)) :
            if (lboard[i] == 'W') :
                lboard[i] = 'B'
                continue
            if (lboard[i] == 'B') :
                lboard[i] = 'W'
            i += 1
        return lboard
    @staticmethod
    def main( args) :
        fInputFile =  java.io.File(args[0])
        fOutputFile =  java.io.File(args[1])
        depth = int(args[2])
        try :
            fis =  java.io.FileInputStream(fInputFile)
            out =  java.io.PrintWriter( java.io.FileWriter(fOutputFile))
            s =  "Python-inputs"
            while (s.hasNextLine()) :
                str = input()
                b = list(str)
                m = MiniMaxGame()
                a = m.MaxMin(b, depth)
                print("" + str(m.positions_evaluated))
                print("" + str(m.minimax_estimate))
                out.println("Board Position : " +  ''.join(a))
                out.println("Positions evaluated by static estimation : " + str(m.positions_evaluated))
                out.println("MiniMax estimate : " + str(m.minimax_estimate))
            fis.close()
            out.close()
        except java.io.IOException as e :
            self.e.printStackTrace()


if __name__=="__main__":
    MiniMaxGame.main(sys.argv)