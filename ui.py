from PyQt5.QtWidgets import *
import sys
import time
from form import *


class GameUi(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(GameUi, self).__init__(parent)
        self.setupUi(self)
        self.game = None
        # self.action_exit.triggered.connect(self.onExitTriggered)
        # self.action_copy.triggered.connect(self.onCopyTriggered)
        # self.action_paste.triggered.connect(self.onPasteTriggered)
        # self.action_cut.triggered.connect(self.onCutTriggered)
        self.btn = [0]*15
        self.cardlb = [0]*15
        self.btngourp = QButtonGroup()
        self.btngourp.addButton(self.btn_card0, 0)
        self.btngourp.addButton(self.btn_card1, 1)
        self.btngourp.addButton(self.btn_card2, 2)
        self.btngourp.addButton(self.btn_card3, 3)
        self.btngourp.addButton(self.btn_card4, 4)
        self.btngourp.addButton(self.btn_card5, 5)
        self.btngourp.addButton(self.btn_card6, 6)
        self.btngourp.addButton(self.btn_card7, 7)
        self.btngourp.addButton(self.btn_card8, 8)
        self.btngourp.addButton(self.btn_card9, 9)
        self.btngourp.addButton(self.btn_card10, 10)
        self.btngourp.addButton(self.btn_card11, 11)
        self.btngourp.addButton(self.btn_card12, 12)
        self.btngourp.addButton(self.btn_card13, 13)
        self.btngourp.addButton(self.btn_card14, 14)

        self.btn[0] = self.btn_card0
        self.btn[1] = self.btn_card1
        self.btn[2] = self.btn_card2
        self.btn[3] = self.btn_card3
        self.btn[4] = self.btn_card4
        self.btn[5] = self.btn_card5
        self.btn[6] = self.btn_card6
        self.btn[7] = self.btn_card7
        self.btn[8] = self.btn_card8
        self.btn[9] = self.btn_card9
        self.btn[10] = self.btn_card10
        self.btn[11] = self.btn_card11
        self.btn[12] = self.btn_card12
        self.btn[13] = self.btn_card13
        self.btn[14] = self.btn_card14
        self.cardlb[0] = self.lb_card0
        self.cardlb[1] = self.lb_card1
        self.cardlb[2] = self.lb_card2
        self.cardlb[3] = self.lb_card3
        self.cardlb[4] = self.lb_card4
        self.cardlb[5] = self.lb_card5
        self.cardlb[6] = self.lb_card6
        self.cardlb[7] = self.lb_card7
        self.cardlb[8] = self.lb_card8
        self.cardlb[9] = self.lb_card9
        self.cardlb[10] = self.lb_card10
        self.cardlb[11] = self.lb_card11
        self.cardlb[12] = self.lb_card12
        self.cardlb[13] = self.lb_card13
        self.cardlb[14] = self.lb_card14

        self.btn_exit.clicked.connect(self.onBtnExitClicked)
        self.btngourp.buttonClicked[int].connect(self.onBtnGroupClicked)
        self.btn_next.clicked.connect(self.onBtnNextClicked)
        self.btn_giveup.clicked.connect(self.onBtnGiveupClicked)
        self.btn_discard.clicked.connect(self.onBtnDiscardClicked)
        self.btn_gettaiji.clicked.connect(self.onBtnGettaijiClicked)
        self.btn_getyangyu.clicked.connect(self.onBtnGetyangyuClicked)
        self.btn_getyinyu.clicked.connect(self.onBtnGetyinyuClicked)
        self.updateCardlb([])

    def updatebtn(self):
        self.updateCardlb(self.game.playerlist[self.game.activePlayer].cardlist)
        if self.game.hasplay == True:
            self.disableBtn()
            self.btn_next.setEnabled(True)
            return
        self.btn_next.setEnabled(False)
        self.enableBtn()

        if self.game.playStatus == 0:
            self.updateCardlb(self.game.playerlist[self.game.activePlayer].cardlist)
            self.btn_gettaiji.setEnabled(self.game.canSnatch_taiji())
            self.btn_getyangyu.setEnabled(self.game.canSnatch_yangyu())
            self.btn_getyinyu.setEnabled(self.game.canSnatch_yinyu())
            self.btn_discard.setText("弃牌模式|OFF")
        elif self.game.playStatus == 1:
            self.updateCardlb(self.game.playerlist[self.game.activePlayer].cardlist,checkv=False)
            self.btn_giveup.setEnabled(False)
            self.btn_gettaiji.setEnabled(False)
            self.btn_getyangyu.setEnabled(False)
            self.btn_getyinyu.setEnabled(False)
            self.btn_discard.setText("弃牌模式|ON")


    def updateCardlb(self,cardlist,checkv = True):
        for btn in self.btn:
            btn.setText('-')
            btn.setEnabled(False)
        if len(cardlist) == 0:
            return
        for i,card in enumerate(cardlist):
            self.btn[i].setText(card.name)
            if self.game.playValidate(card):
                self.btn[i].setEnabled(True)
            else:
                if checkv:
                    self.btn[i].setEnabled(False)
                else:
                    self.btn[i].setEnabled(True)

    def updateGamelog(self,str):
        self.tb_log.setText(str)

    def disableBtn(self):
        for btn in self.btn:
            btn.setEnabled(False)
            self.btn_giveup.setEnabled(False)
            self.btn_discard.setEnabled(False)
            self.btn_gettaiji.setEnabled(False)
            self.btn_getyangyu.setEnabled(False)
            self.btn_getyinyu.setEnabled(False)


    def enableBtn(self):
        for btn in self.btn:
            btn.setEnabled(True)
            self.btn_giveup.setEnabled(True)
            self.btn_discard.setEnabled(True)

    def onBtnGroupClicked(self,i):
        p = self.game.playerlist[self.game.activePlayer]
        h = self.game.h
        sel = i
        if self.game.playStatus == 0 and self.game.hasplay == False:
            selcard = p.cardlist[int(sel)]
            if self.game.playValidate(selcard):
                self.game.log = '玩家%s出牌:%s,抽取3张牌\n'%(p.name,selcard.name) + self.game.log
                p.discardcard(h, sel)
                self.game.lastcard = selcard
                p.get3card(h)
                self.updateCardlb(p.cardlist)
                self.game.hasplay = True
            else:
                print('不合理出牌')
        if self.game.playStatus == 1:
            selcard = p.cardlist[int(sel)]
            p.discardcard(h, sel)
            self.game.log = '玩家%s丢弃:%s\n' % (p.name, selcard.name) + self.game.log
        self.updatebtn()
        self.updateGamelog(self.game.log)

    def onBtnDiscardClicked(self):
        if (self.game.playStatus == 0): self.game.playStatus = 1 #进入弃牌模式
        elif (self.game.playStatus == 1): self.game.playStatus = 0  # 退出弃牌模式
        self.updatebtn()

    def onBtnGiveupClicked(self):
        p = self.game.playerlist[self.game.activePlayer]
        h = self.game.h
        if self.game.playStatus == 0 and self.game.hasplay == False:
            self.game.log = '玩家%s放弃出牌,抽取1张牌\n'% (p.name) + self.game.log
            p.getcard(h)
            self.updateCardlb(p.cardlist)
            self.game.hasplay = True
        self.updatebtn()
        self.updateGamelog(self.game.log)

    def onBtnGetyangyuClicked(self):
        p = self.game.playerlist[self.game.activePlayer]
        result = self.game.Snatch((0, 1, 1, 0))
        if result!=False:
            self.game.log = '玩家%s从玩家%s手中抢夺了阳鱼\n' % (p.name,result.name)+ self.game.log
        else:
            self.game.log = '玩家%s抢夺阳鱼失败\n' % (p.name) + self.game.log
        self.game.hasplay = True
        self.updatebtn()
        self.updateGamelog(self.game.log)

    def onBtnGetyinyuClicked(self):
        p = self.game.playerlist[self.game.activePlayer]
        result = self.game.Snatch((0, 1, 0, 0))
        if result != False:
            self.game.log = '玩家%s从玩家%s手中抢夺了阴鱼\n' % (p.name, result.name) + self.game.log
        else:
            self.game.log = '玩家%s抢夺阴鱼失败\n' % (p.name) + self.game.log
        self.game.hasplay = True
        self.updatebtn()
        self.updateGamelog(self.game.log)

    def onBtnGettaijiClicked(self):
        p = self.game.playerlist[self.game.activePlayer]
        result = self.game.Snatch((0, 0, 0, 0))
        if result !=False:
            self.game.log = '玩家%s从玩家%s手中抢夺了太极\n' % (p.name, result.name) + self.game.log
        else:
            self.game.log = '玩家%s抢夺太极失败\n' % (p.name) + self.game.log
        self.game.hasplay = True
        self.updatebtn()
        self.updateGamelog(self.game.log)

    def onBtnNextClicked(self):
        self.game.nextTurn()

    def onBtnExitClicked(self):
        exit()

# app = QApplication(sys.argv)
# ui = GameUi()
# ui.show()
# sys.exit(app.exec_())