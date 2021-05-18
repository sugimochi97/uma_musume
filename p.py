#%%
STATUS_BASE = 1  # ステータス１に対しての価値
STATUS_UP = 1.2 # ステータスに対して、重要なステータスの上振れ率
STATUS_DOWN = 0.8 # ステータスに対して、重要でないステータスの下振れ率
# スピード、スタミナ、パワー、根性（いらないのでとりあえず下げてる）、賢さの価値
STATUS_ALL = [STATUS_BASE, STATUS_BASE, STATUS_BASE, STATUS_BASE*STATUS_DOWN, STATUS_BASE]

BONDS_PER = 1/4 # 絆ゲージが溜まっていない場合、ゲージ進行度別の価値割合
BONDS_UP = 1.2 # 友情トレーニングの時の平均ステータス上昇率
BONDS_BASE = 10 # 友情トレーニングの価値計算の時に使う基礎値
# 友情トレーニングを行った時の価値計算(１枚、２枚、３枚)
BONDS_VALUE = [BONDS_UP*BONDS_BASE, BONDS_UP**2*BONDS_BASE, BONDS_BASE**3*BONDS_UP]
# 上記の価値に対して、ゲージ進行度に関数る割合をかけて絆ゲージをあげる価値と定める

PHYSICAL_PER = 2/3 # 体力に対する価値(p計算法からそのまま引用)
SKILL_PER = 2/5 # スキルに対する価値(p計算法からそのまま引用)

TIPS_STATUS_UP_PER = 0.3 # ヒントで得られるステータスorスキルでの割合
TIPS_SKILL_PER = 0.7
TIPS_STATUS_VALUE = (6+2)*TIPS_STATUS_UP_PER # ヒントでもらえるステータス価値
TIPS_SKILL_VALUE_USE = 10*TIPS_SKILL_PER # ヒントで得られるスキルが欲しいものかどうか(確率無視)
TIPS_SKILL_VALUE_NO = 3*TIPS_SKILL_PER
TIPS_BONDS_PER = 5/7 # ヒントによる絆ゲージアップの恩恵（5ポイントUPするのでその割合）
TIPS_BONDS_VALUE = BONDS_VALUE[0]*TIPS_BONDS_PER # ヒントによる絆ゲージアップの価値
TIPS_USE_VALUE = TIPS_STATUS_VALUE+TIPS_SKILL_VALUE_USE # 使えるスキルのヒント価値
TIPS_NO_VALUE = TIPS_STATUS_VALUE+TIPS_SKILL_VALUE_NO # 使えないスキルのヒント価値
# この価値に対して、絆ゲージの価値を現状の割合（BONDS_PER）でかけた値を足して価値として計算可能

CONDITION_PER = [1.2, 1.1, 1.0, 0.9, 0.8] # 調子ごとのステータス影響率
CONDITION_BASE = 20 # 調子のベース価値
# 未来に起こる減少イベントは無視（予測不可）
# あくまで現在の調子から、お出かけなどをする価値があるのかを計算する
CONDITION_EVENT = [0.3, 0.7] # お出かけによる２UPと１UPの割合をざっくり
# 1.2 = 5ターンにつき、１ターン分の利益
# 1.1 = １０ターンにつき、１ターン分の利益 逆は損失
# 計算めんどなったので、とりあえず引用しておく
CONDITION_VALUE = 15

# 機会に関しても計算めんどくさいのでそのまま引用
OP_MAIN = 40
OP_SUB = 30
OP_OTHER = 15



class P:
    def __init__(self, s=STATUS_ALL, b=BONDS_VALUE, pp=PHYSICAL_PER, sp=SKILL_PER, tuv=TIPS_USE_VALUE,
                tnv=TIPS_NO_VALUE, cv=CONDITION_VALUE, om=OP_MAIN, os=OP_SUB, oo=OP_OTHER):
        self.status = s
        self.bonds = b
        self.physical_per = pp
        self.skill_per = sp
        self.tips = [tuv, tnv, 0]
        self.condition_v = cv
        self.op = [om, os, oo]

    def calc(self, status_up, skill_up=3, op=0, tips=2, condition=0, bonds1=0, bonds2=0, bonds3=0, physical=25):
        '''
        引数 :
            op : メイン(0)サブ(1)その他(2)を指定
            status_up : ステータスの上昇値（必須）
            tips : 欲しい(0)欲しくない(1)なし(2)
            consdition : 増加があり(1)なし(0)、減少は(-1)
            bonds : 溜めているゲージの数、繰り上げ(0 > 1, 1 > 2, 2 > 3, 3 > 4、４超過は入力なし(0))
            他は数値
        '''
        b = self.bonds*bonds1 + self.bonds*bonds2 + self.bonds*bonds3

        self.result = status_up + physical*self.physical_per + skill_up*self.skill_per + self.tips[tips] \
            + self.condition_v*condition + self.op[op] + b

        return self.result
# %%
