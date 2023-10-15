import numpy as np
import random

# 共通関数
class CommonFunc():
    def __init__(self):
        self.n1 = random.randrange(1,10)
        self.n2 = random.randrange(1,10)
        self.n3 = random.randrange(1,10)
        self.n4 = random.randrange(1,10)

     # 盤面固定用関数
    def updateField(self, field):
        posList = self.moveMinoPos(field)
        for pos in posList:
            field[pos[0]] = self.mino[pos[1]]
        pass

    # ミノ移動用関数
    def moveMinoPos(self, field, origin=None, block=None):
        if(origin == None):
            origin = self.base

        if(type(block) != np.ndarray):
            block = self.mino

        row, col = np.shape(block)
        rowMax, colMax = np.shape(field)
        rowBase, colBase = origin
        posList = []

        for i in range(0, row):
            for j in range(0, col):
                num = block[(i, j)]
                rpos = rowBase + i
                cpos = colBase + j

                if(num != 0):
                    if(num != 0):
                        if(not (0 <= rpos <= rowMax-2 or 1 <= cpos <= colMax-2)):
                            return []
                        if(field[(rpos, cpos)] != 0):
                            return []
                        posList.append(((rpos, cpos), (i, j)))
        return posList

    # ミノ左回転用関数
    def rollLeft(self, field):
        block = self.pattern[(self.count + 1) % 4]
        posList = self.moveMinoPos(field, block=block)
        if(len(posList) != 0):
            self.count = (self.count + 1) % 4
            self.mino = self.pattern[self.count]
            return True
        return False

    # ミノ右回転用関数
    def rollRight(self, field):
        block = self.pattern[(self.count + 3) % 4]
        posList = self.moveMinoPos(field, block=block)
        if(len(posList) != 0):
            self.count = (self.count + 3) % 4
            self.mino = self.pattern[self.count]
            return True
        return False
