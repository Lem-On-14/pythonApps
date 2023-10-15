import numpy as np
import random
from common.mino import Imino, Jmino, Lmino, Omino, Smino, Tmino, Zmino

class GM():

    # 削除する座標を算出する関数
    def getdelPosList(self, field):
        offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        posList = list(zip(*np.where((field != 10) & (field != 0))))
        delPosList = []
        for pos in posList:
            for i in offset:
                npos = (pos[0] + i[0], pos[1] + i[1])
                if((field[pos] + field[npos]) == 10):
                    delPosList.append(npos)
                    delPosList.append(pos)
        delPosList = list(set(delPosList))
        return delPosList

    # 実際に数字を下げる関数
    def downNum(self, field, posList):
        downPosDict = {}    # col : [row1, row2]
        for pos in posList:
            row, col = pos[0], pos[1]
            if(col not in downPosDict):
                downPosDict[col] = [row]
            elif(col in downPosDict):
                downPosDict[col].append(row)
            else:
                print("downNum\nError : in / not in")
        for key in downPosDict.keys():
            temp = field[:, key]
            delList = sorted(downPosDict[key], reverse=True)
            zeroList = []
            for idx in delList:
                temp = np.delete(temp, idx)
                zeroList.append(0)
            temp = np.insert(temp, 0, zeroList)
            field[:, key] = temp
        pass

    def checkExitCond(self, field, pos):
        # check exit condition
        # fieldにおけるposにある数字がゼロであるとき
        # 終了していないときは、Falseを返す
        # 終了しているときは、Trueを返す
        num = field[pos]
        if(num == 0):
            return False
        return True

    def getRandomMino():
        minoList = [Imino(), Jmino(), Lmino(), Omino(), Smino(), Tmino(), Zmino()]
        r = random.randrange(0, len(minoList))
        return minoList[r]