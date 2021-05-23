#%%
import pandas as pd
import numpy as np

RACE_RESULT_PATH = 'race_result_ver1.0.1.csv'
TEAME_DATA_PATH = 'team_data_ver1.0.0.csv'
NORMAL_SKILL_PATH = 'team_race_normal_skill_point.csv'
UNIQUE_SKILL_PATH = 'team_race_unique_skill_point.csv'
RANK_POINT_PATH = 'team_race_rank_point.csv'
TEAM_BONUS_PATH = 'team_race_team_bonus_point.csv'

ACE_BONUS = 1.1

class TeamRace:
    def __init__(self):
        self.df_result = pd.read_csv(RACE_RESULT_PATH)
        self.df_team_data = pd.read_csv(TEAME_DATA_PATH)
        self.df_skill_point = pd.read_csv(NORMAL_SKILL_PATH, index_col=0)
        self.df_unique_skill = pd.read_csv(UNIQUE_SKILL_PATH)
        self.df_rank_point = pd.read_csv(RANK_POINT_PATH, index_col=0)
        self.df_bonus_point = pd.read_csv(TEAM_BONUS_PATH)
        
        # チームボーナスを読み込む
        with open(RACE_RESULT_PATH, 'r', encoding='utf-8') as obj:
            obj_read = obj.readlines()
            if len(obj_read) >= 22:
                self.team_bonus = int(obj_read[-1].rstrip(','))

        self.df_result = self.df_result.dropna(how='any')
        self.df_result.iloc[:, 1:12] = self.df_result.iloc[:, 1:12].astype(int)
        

    def calc_score(self):
        # 順位ポイントの算出
        ranks = list(self.df_result.iloc[:, 1])
        rank_points = [int(self.df_rank_point.loc[i]) for i in ranks]

        rank_points = np.array(rank_points)

        # 固有スキルポイントを呼び出す
        uni_skill_result = []
        for i in self.df_result.iloc[:, 2:4].itertuples():
            uni_skill_result.append((i[1], i[2]))

        # 固有スキルポイントの算出
        uni_skill_point = []
        for i, j in uni_skill_result:
            df = self.df_unique_skill[self.df_unique_skill['レアリティ'] == i]
            df = df[df['スキルLv'] == j]
            uni_skill_point.append(int(df['獲得基礎スコア']))
        
        uni_skill_point = np.array(uni_skill_point)

        # 金スキルと白スキルの算出
        rare_skill_result = self.df_result['発動スキル金']
        norm_skill_result = self.df_result['発動スキル白']

        rare_skill_point = int(self.df_skill_point.loc['レアスキル']) * \
                            rare_skill_result
        norm_skill_point = int(self.df_skill_point.loc['通常スキル']) * \
                            norm_skill_result

        rare_skill_point = np.array(rare_skill_point)
        norm_skill_point = np.array(norm_skill_point)

        # 着差
        diffrence_point = np.array(self.df_result['着差'])

        # 基準タイム越え
        over_time_point = np.array(self.df_result['基準タイム越え'])

        # スタートダッシュ
        start_point = np.array(self.df_result['スタートダッシュ'])

        # ナイスポジション
        position_point = np.array(self.df_result['ナイスポジション'])

        # マイナス
        minus_point = np.array(self.df_result['マイナス'])

        # 基礎スコアを足す
        self.score = rank_points + uni_skill_point + rare_skill_point + norm_skill_point + \
                        diffrence_point + over_time_point + start_point + position_point + minus_point
        
        # ndarrayの型を浮動小数点に変更
        self.score = self.score.astype(np.float)
        self.base_score = self.score.copy()

        # エース倍率をかける
        self.score[::3] *= ACE_BONUS
        self.score.round()
        print(self.score)

        # 連勝数の倍率をかける
        self.score += (self.base_score * np.array(self.df_result['連勝数'], dtype=np.float)/100+1).round()
        print(self.score)

        # 対戦相手ボーナスをかける
        self.score += (self.base_score * (np.array(self.df_result['対戦相手ボーナス'], dtype=np.float)-1)).round()
        print(self.score)

        # サポート割合をかける
        self.score += (self.base_score * (np.array(self.df_result['サポート割合'], dtype=np.float)-1)).round()
        print(self.score)

        print(self.score.sum() + self.team_bonus)

        

t = TeamRace()
t.calc_score()
# %%
