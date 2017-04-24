# coding=UTF-8
cardDic = {
    (0, 0, 0, 0): ' ◐ 太极 ',
    (0, 1, 0, 0): ' ♠ 阴鱼 ',
    (0, 1, 1, 0): ' ♤ 阳鱼 ',
    (0, 2, 0, 0): ' ○ 青龙 ',
    (0, 2, 1, 0): ' ○ 白虎 ',
    (0, 2, 2, 0): ' ○ 朱雀 ',
    (0, 2, 3, 0): ' ○ 玄武 ',
    (0, 2, 0, 1): ' ● 青龙 ',
    (0, 2, 1, 1): ' ● 白虎 ',
    (0, 2, 2, 1): ' ● 朱雀 ',
    (0, 2, 3, 1): ' ● 玄武 ',
    (0, 3, 0, 0): '  □ 天  ',
    (0, 3, 1, 0): '  □ 地  ',
    (0, 3, 2, 0): '  □ 风  ',
    (0, 3, 3, 0): '  □ 雷  ',
    (0, 3, 4, 0): '  □ 水  ',
    (0, 3, 5, 0): '  □ 火  ',
    (0, 3, 6, 0): '  □ 山  ',
    (0, 3, 7, 0): '  □ 泽  ',
    (0, 3, 0, 1): '  ■ 天  ',
    (0, 3, 1, 1): '  ■ 地  ',
    (0, 3, 2, 1): '  ■ 风  ',
    (0, 3, 3, 1): '  ■ 雷  ',
    (0, 3, 4, 1): '  ■ 水  ',
    (0, 3, 5, 1): '  ■ 火  ',
    (0, 3, 6, 1): '  ■ 山  ',
    (0, 3, 7, 1): '  ■ 泽  ',
    (1, 0, 0, 0): '偷天换日',
    #(1, 0, 0, 0): '见风是雨',
    (1, 1, 0, 0): '三才杀机',
    (1, 2, 0, 0): '斗转星移',
    (1, 3, 0, 0): '阴阳共济',
    (1, 4, 0, 0): '卜天算地'
}

class NormalCard:
    def __init__(self, type, subtype, yinyang):
        self.type = (0 ,type, subtype, yinyang)
        self.name = cardDic[self.type]
    def compare(self,card):
        if self.type[0] == 1:
            return False
        if self.type[1] < card.type[1]:
            return True
        elif self.type[1] == card.type[1]:
            if card.type[2] == 2 ** self.type[1] - 1 and self.type[2] == 0:
                return True
            if self.type[2] == 2 ** card.type[1] - 1 and card.type[2] == 0:
                return False
            if self.type[2] == card.type[2] + 1:
                return True
            else:
                return False
        else:
            return False

class SpecialCard:
    def __init__(self, type):
        self.type = (1, type, 0 , 0)
        self.name = cardDic[self.type]