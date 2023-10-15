import numpy as np
import random
import sys
from Common.common import CommonFunc

class Computer(CommonFunc):
    def electRandom(self, field):
        pl = self.getPossibleLocation(field)
        if(len(pl) == 0):
            print("pass")
            return
        r = random.randrange(0, len(pl))
        for i in enumerate(pl):
            if(i[0] == r):
                return i[1]
        print("Error : electRandom")
        sys.exit()
