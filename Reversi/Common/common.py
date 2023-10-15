import numpy as np
import random
import sys

class CommonFunc():

    global offset
    offset = [(-1, -1), (-1, 0), (-1, 1),
          ( 0, -1),          ( 0, 1),
          ( 1, -1), ( 1, 0), ( 1, 1)]

    def __init__(self, mystone, opponentstone):
        self.mystone = mystone
        self.opponentstone = opponentstone

    # 相手stoneの座標のリストを返す
    def getStoneLocation(self, field):
        locaList = list(zip(*np.where(field == self.opponentstone)))
        return locaList

    # 相手stoneの隣マスの座標のリストを返す
    def getNextLocation(self, field):
        sl = self.getStoneLocation(field)
        locaList = []
        for x, y in sl:
            for i, j in offset:
                t = (x + i, y + j)
                locaList.append(t)
        return locaList

    # 空のマスを返す
    def getEmptyLocation(self, field):
        locaList = list(zip(*np.where(field == 0)))
        return locaList

    # 石を置くことができるマスを返す
    def getPossibleLocation(self, field):
        nextLocation = self.getNextLocation(field)
        emptyLocation = self.getEmptyLocation(field)

        # 石がない座標と相手の石の隣のマスの座標が一致するリスト(setで重複は削除)
        nextAndEmptyList = list(set(nextLocation) & set(emptyLocation))

        # 石をおける座標を取得(Key:座標, Value:方向)
        possibleLocaDict = {}
        for x, y in nextAndEmptyList:

            # nextAndEmptyListの位置に石を置いた場所から自身の石があるかを8方向で探索
            getPossibleOpponentstoneLocaList = []
            for i, j in offset:
                xpos, ypos = x + i, y + j
                tmpPossibleLoca = []
                isFieldOutFlg = True
                # フィールド内である限り探索
                while ((0 <= xpos < field.shape[0]) and (0 <= ypos < field.shape[1])):
                    # 相手の石がある場合は探索している方向に更に進んで探索
                    if(field[xpos, ypos] == self.opponentstone):
                        tmpPossibleLoca.append((xpos, ypos))
                        xpos = xpos + i
                        ypos = ypos + j
                        continue
                    # 自身の石がある場合
                    elif(field[xpos, ypos] == self.mystone):
                        isFieldOutFlg = False
                        break
                    # 石がないまたは自身の石がある場合
                    else:
                        break
                # 自分の置いた石の先に自分の石があるかつ置いた石のすぐ隣が自分の石でない場合
                if(not isFieldOutFlg):
                    # 置いた石のすぐ隣が自分の石の場合はループに入らない
                    for loca in tmpPossibleLoca:
                        getPossibleOpponentstoneLocaList.append(loca)
            if (len(getPossibleOpponentstoneLocaList) != 0):
                possibleLocaDict[x, y] = getPossibleOpponentstoneLocaList
        return possibleLocaDict

    def updateField(self, pos, field):
        # fieldの更新
        possibleDict = self.getPossibleLocation(field)
        field[pos[0], pos[1]] = self.mystone
        # 相手の石をひっくり返す
        for xpos, ypos in possibleDict[pos]:
            if(field[xpos, ypos] == self.opponentstone):
                field[xpos, ypos] = self.mystone
            else:
                break