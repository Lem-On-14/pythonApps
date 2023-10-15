from common.tenplus import CommonFunc
import numpy as np
import random

# Iミノ
class Imino(CommonFunc):
    def __init__(self):
        super(Imino, self).__init__()
        self.base = (1, 4) # fieldにおけるミノの左上の座標
        self.count = 0
        self.pattern = np.array([[[0, self.n1, 0, 0],
                                  [0, self.n2, 0, 0],
                                  [0, self.n3, 0, 0],
                                  [0, self.n4, 0, 0]],
                                 [[      0,       0,       0,       0],
                                  [self.n1, self.n2, self.n3, self.n4],
                                  [      0,       0,       0,       0],
                                  [      0,       0,       0,       0]],
                                 [[0, 0, self.n4, 0],
                                  [0, 0, self.n3, 0],
                                  [0, 0, self.n2, 0],
                                  [0, 0, self.n1, 0]],
                                 [[      0,       0,       0,       0],
                                  [      0,       0,       0,       0],
                                  [self.n4, self.n3, self.n2, self.n1],
                                  [      0,       0,       0,       0]]])
        self.mino = self.pattern[0]

# Jミノ
class Jmino(CommonFunc):
    def __init__(self):
        super(Jmino, self).__init__()
        self.base = (2, 5)
        self.count = 0
        self.pattern = np.array([[[      0, self.n1, 0],
                                  [      0, self.n2, 0],
                                  [self.n4, self.n3, 0]],
                                 [[      0,       0,       0],
                                  [self.n1, self.n2, self.n3],
                                  [      0,       0, self.n4]],
                                 [[0, self.n3, self.n4],
                                  [0, self.n2,       0],
                                  [0, self.n1,       0]],
                                 [[self.n4,       0,       0],
                                  [self.n3, self.n2, self.n1],
                                  [      0,       0,       0]]])
        self.mino = self.pattern[0]

# Lミノ
class Lmino(CommonFunc):
    def __init__(self):
        super(Lmino, self).__init__()
        self.base = (2, 4)
        self.count = 0
        self.pattern = np.array([[[0, self.n1,       0],
                                  [0, self.n2,       0],
                                  [0, self.n3, self.n4]],
                                 [[      0,       0, self.n4],
                                  [self.n1, self.n2, self.n3],
                                  [      0,       0,       0]],
                                 [[self.n4, self.n3, 0],
                                  [      0, self.n2, 0],
                                  [      0, self.n1, 0]],
                                 [[      0,       0,       0],
                                  [self.n3, self.n2, self.n1],
                                  [self.n4,       0,       0]]])
        self.mino = self.pattern[0]

# Oミノ
class Omino(CommonFunc):
    def __init__(self):
        super(Omino, self).__init__()
        self.base = (2, 4)
        self.count = 0
        self.pattern = np.array([[[0,       0,       0, 0],
                                  [0, self.n1, self.n2, 0],
                                  [0, self.n3, self.n4, 0],
                                  [0,       0,       0, 0]],
                                 [[0,       0,       0, 0],
                                  [0, self.n2, self.n4, 0],
                                  [0, self.n1, self.n3, 0],
                                  [0,       0,       0, 0]],
                                 [[0,       0,       0, 0],
                                  [0, self.n4, self.n3, 0],
                                  [0, self.n2, self.n1, 0],
                                  [0,       0,       0, 0]],
                                 [[0,       0,       0, 0],
                                  [0, self.n3, self.n1, 0],
                                  [0, self.n4, self.n2, 0],
                                  [0,       0,       0, 0]]])
        self.mino = self.pattern[0]

# Sミノ
class Smino(CommonFunc):
    def __init__(self):
        super(Smino, self).__init__()
        self.base = (3, 5)
        self.count = 0
        self.pattern = np.array([[[      0, self.n2, self.n1],
                                  [self.n4, self.n3,       0],
                                  [      0,       0,       0]],
                                 [[self.n1,       0, 0],
                                  [self.n2, self.n3, 0],
                                  [      0, self.n4, 0]],
                                 [[      0,       0,       0],
                                  [      0, self.n3, self.n4],
                                  [self.n1, self.n2,       0]],
                                 [[0, self.n4,       0],
                                  [0, self.n3, self.n2],
                                  [0,       0, self.n1]]])
        self.mino = self.pattern[0]

# Tミノ
class Tmino(CommonFunc):
    def __init__(self):
        super(Tmino, self).__init__()
        self.base = (2, 4)
        self.count = 0
        self.pattern = np.array([[[      0,       0,       0],
                                  [self.n1, self.n2, self.n3],
                                  [      0, self.n4,       0]],
                                 [[0, self.n3,       0],
                                  [0, self.n2, self.n4],
                                  [0, self.n1,       0]],
                                 [[      0, self.n4,       0],
                                  [self.n3, self.n2, self.n1],
                                  [      0,       0,       0]],
                                 [[      0, self.n1, 0],
                                  [self.n4, self.n2, 0],
                                  [      0, self.n3, 0]]])
        self.mino = self.pattern[0]

# Zミノ
class Zmino(CommonFunc):
    def __init__(self):
        super(Zmino, self).__init__()
        self.base = (3, 4)
        self.count = 0
        self.pattern = np.array([[[self.n1, self.n2,       0],
                                  [      0, self.n3, self.n4],
                                  [      0,       0,       0]],
                                 [[      0, self.n4, 0],
                                  [self.n2, self.n3, 0],
                                  [self.n1,       0, 0]],
                                 [[      0,       0,       0],
                                  [self.n4, self.n3,       0],
                                  [      0, self.n2, self.n1]],
                                 [[0,       0, self.n1],
                                  [0, self.n3, self.n2],
                                  [0, self.n4,       0]]])
        self.mino = self.pattern[0]