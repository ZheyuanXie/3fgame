from player import player
from cards import NormalCard,SpecialCard
from heap import heap
from ui import *
import sys
from PyQt5.QtWidgets import *

class game:
    def __init__(self,playerlist,ui):
        self.ui = ui
        self.h = heap()
        self.h.displayallcard()
        self.playerlist = playerlist
        print('---------初始手牌---------')
        for p in self.playerlist:
            p.get5card(self.h)
            p.displayallcard()

        self.turncnt = 1
        self.activePlayer = -1
        self.lastcard = None
        self.playStatus = 0 #0-出牌，1-弃牌
        self.hasplay = False
        self.log = ''

    def nextTurn(self):
        if self.activePlayer == len(self.playerlist) - 1:
            self.turncnt += 1
            self.activePlayer = 0
        else:
            self.activePlayer += 1
        p = self.playerlist[self.activePlayer]
        print('---------回合%03d玩家%s---------'%(self.turncnt,p.name))
        self.playStatus = 0
        self.hasplay = False
        self.ui.lb_activeplayer.setText('当前是玩家'+p.name+'的回合')
        self.ui.updatebtn()

            # if self.lastcard == None:
            #     print('现在是玩家%d(%s)的回合' % (i + 1, p.name))
            # else:
            #     print('现在是玩家%d(%s)的回合,上一张牌:%s' % (i + 1, p.name, self.lastcard.name))
            # p.displayallcard()
            # ui.updateCardlb(p.cardlist)
            # while 1:
            #     sel = str(input('请选择手牌(x=放弃）:'))
            #     if sel == 'x':
            #         print('玩家%d(%s)放弃出牌,抽取1张牌'% (i + 1, p.name))
            #         self.log = '玩家%d(%s)放弃出牌,抽取1张牌\n'% (i + 1, p.name) + self.log
            #         p.getcard(self.h)
            #         break
            #     selcard = p.cardlist[int(sel) - 1]
            #     if self.playValidate(selcard):
            #         print('玩家%d(%s)出牌:%s,抽取3张牌'%(i + 1, p.name,selcard.name))
            #         self.log = '玩家%d(%s)出牌:%s,抽取3张牌\n'%(i + 1, p.name,selcard.name) + self.log
            #         p.discardcard(self.h, int(sel))
            #         self.lastcard = selcard
            #         p.get3card(self.h)
            #         break
            #     else:
            #         print('不合理出牌')
            # p.displayallcard()
            # ui.updateGamelog(self.log)
            # print('玩家%d(%s)的回合结束' % (i + 1, p.name))
            # print()
    def canSnatch_yinyu(self):
        # 抢夺阴鱼条件
        b = True
        cards = []
        for item in self.playerlist[self.activePlayer].cardlist:
            cards.append(item.type)
        for i in range(8):
            if (not (0, 3, i, 1) in cards):
                b = False
        return b or self.canSnatch_yu()

    def canSnatch_yangyu(self):
        # 抢夺阳鱼条件
        b = True
        cards = []
        for item in self.playerlist[self.activePlayer].cardlist:
            cards.append(item.type)
        for i in range(8):
            if (not (0, 3, i, 0) in cards):
                b = False
        return b or self.canSnatch_yu()

    def canSnatch_yu(self):
        # 抢夺两仪条件
        b = True
        cards = []
        for item in self.playerlist[self.activePlayer].cardlist:
            cards.append(item.type)
        for i in range(4):
            if (not (0, 2, i, 0) in cards) and (not (0, 2, i, 1) in cards):
                b = False
        return b

    def canSnatch_taiji(self):
        # 抢夺太极条件
        cards = []
        for item in self.playerlist[self.activePlayer].cardlist:
            cards.append(item.type)

        b1 = True
        for i in range(4):
            if (not (0, 2, i, 0) in cards) or (not (0, 2, i, 1) in cards):
                b1 = False
        b2 = True
        for i in range(2):
            if (not (0, 1, i, 0) in cards):
                b2 = False
        return b1 or b2

    def Snatch(self,cardtype):
        pi = self.activePlayer

        while 1:
            pi += 1
            if (pi == len(self.playerlist)): pi = 0
            if pi == self.activePlayer: break
            p_tgt = self.playerlist[pi]
            for i,item in enumerate(p_tgt.cardlist):
                if item.type == cardtype:
                    p_tgt.givecard(self.playerlist[self.activePlayer],i) # 转移手牌
                    return p_tgt
        return False

    def playValidate(self,card):
        if card.type[0] == 1:
            return True
        if self.lastcard == None:
            return True
        else:
            if self.lastcard.type[0] == 1:
                return True
            return card.compare(self.lastcard)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = GameUi()
    ui.show()
    # 三人局
    # playerList = list()
    # playerList.append(player(input('玩家1名称：')))
    # playerList.append(player(input('玩家2名称：')))
    # playerList.append(player(input('玩家3名称：')))
    playerList = [player('a'),player('b'),player('c')]
    g = game(playerList,ui)
    ui.game = g
    g.nextTurn()
    sys.exit(app.exec_())