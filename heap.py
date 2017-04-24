# coding=UTF-8
from cards import *
import random

class heap:
    def __init__(self):
        self.cardlist = []
        self.cardgen()
        self.cardlist.reverse()
        self.shuffle()

    def size(self):
        return len(self.cardlist)

    def shuffle(self):
        random.shuffle(self.cardlist)

    def cardgen(self):
        # 一太极
        self.cardlist.append(NormalCard(0, 0, 0))
        # 四鱼
        self.cardlist.append(NormalCard(1, 0, 0))
        self.cardlist.append(NormalCard(1, 0, 0))
        self.cardlist.append(NormalCard(1, 1, 0))
        self.cardlist.append(NormalCard(1, 1, 0))
        # 十六象
        for j in range(2):
            for i in range(4):
                self.cardlist.append(NormalCard(2, i, j))
                self.cardlist.append(NormalCard(2, i, j))
        # 六十四卦
        for i in range(8):
            for j in range(4):
                self.cardlist.append(NormalCard(3, i, 0))
                self.cardlist.append(NormalCard(3, i, 1))
        # 技能牌
        for i in range(1):
            for j in range(4):
                self.cardlist.append(SpecialCard(i))

    def displayallcard(self):
        print('当前牌堆有%d张牌'%self.size())
        cnt = 0
        for item in self.cardlist:
            if cnt %5 != 4:
                print(item.name, end = ' ')
            else:
                print(item.name, end = '\n')
            cnt+=1
        print()
