# coding=UTF-8
from heap import *

class player:
    def __init__(self,name):
        self.name = name
        self.cardlist = []

    def cardcnt(self):
        return len(self.cardlist)

    def get5card(self,h):
        for i in range(5):
            self.getcard(h)

    def get3card(self,h):
        for i in range(3):
            self.getcard(h)

    def getcard(self,h):
        card = h.cardlist.pop()
        self.cardlist.append(card)

    def discardcard(self,h,i):
        card = self.cardlist.pop(i)
        h.cardlist.append(card)
        h.shuffle()
        return card

    def givecard(self,tgt,i):
        card = self.cardlist.pop(i)
        tgt.cardlist.append(card)
        return card

    def displayallcard(self):
        cnt = 0
        print('【%s的手牌】'%self.name)
        for item in self.cardlist:
            print('%d:%s'%(cnt+1,item.name), end = '|')
            cnt+=1
        print()

# h = heap()
# h.displayallcard()
# p1 = player('xlf')
# p1.get5card(h)
# p1.displayallcard()
# p1.discardcard(h,1)
# p1.displayallcard()