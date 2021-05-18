from tkinter import *
from p import *

SIZE = '800x700'
TITLE = 'ウマ娘 育成用 p計算機'
PIVOT = [40, 20]
SEP = 40
PIVOT_LABEL = [PIVOT[0], PIVOT[1]]
SEP_LABEL = SEP
PIVOT_ELEM = [PIVOT[0]+160, PIVOT[1]]
SEP_ELEM = SEP
RADIO_SEP = 10
INDEX_TRANING = 3
INDEX_TIPS = 4
INDEX_CONDITION = 5
SEP_RADIO_TRANING = 120
SEP_RADIO_TIPS = 120
SEP_RADIO_CONDITION = 120
SEP_RADIO_BONDS = 50

class P_APP(P):
    def __init__(self):
        super().__init__()
        self.tk = Tk()
        self.labels = [Label(text='ステータス上昇量'),
                        Label(text='スキルポイント上昇量'),
                        Label(text='体力消費'),
                        Label(text='行うトレーニング'),
                        Label(text='ヒントの有無'),
                        Label(text='調子が下がるか上がるか'),
                        Label(text='絆ゲージ１'),
                        Label(text='絆ゲージ２'),
                        Label(text='絆ゲージ３'),
                        Label(text='結果'),]
        # self.labels = {'status':Label(text='ステータス上昇量'),
        #                 'skill':Label(text='スキルポイント上昇量'),
        #                 'traning':Label(text='行うトレーニング'),
        #                 'tips':Label(text='ヒントの有無'),
        #                 'condition':Label(text='調子が下がるか上がるか'),
        #                 'bonds1':Label(text='絆ゲージ１'),
        #                 'bonds2':Label(text='絆ゲージ２'),
        #                 'bonds3':Label(text='絆ゲージ３'),
        #                 'physical':Label(text='体力消費'),
        #                 'result':Label(text='結果')}
        self.status_entry = Entry(width=20)
        self.status_entry.insert(0, '0')
        self.skill_entry = Entry(width=20)
        self.skill_entry.insert(0, '0')
        self.physical_entry = Entry(width=20)
        self.physical_entry.insert(0, '0')
        self.traning_var = IntVar()
        self.traning_var.set(0)
        self.traning_btns = [Radiobutton(self.tk, value=0, variable=self.traning_var, text='メイン'), 
                                Radiobutton(self.tk, value=1, variable=self.traning_var, text='サブ'),
                                Radiobutton(self.tk, value=2, variable=self.traning_var, text='その他'),]
        self.tips_var = IntVar()
        self.tips_var.set(0)
        self.tips_btns = [Radiobutton(self.tk, value=0, variable=self.tips_var, text='使うスキル'), 
                            Radiobutton(self.tk, value=1, variable=self.tips_var, text='使わないスキル'),
                            Radiobutton(self.tk, value=2, variable=self.tips_var, text='なし'),]
        self.condition_var = IntVar()
        self.condition_var.set(0)
        self.condition_btns = [Radiobutton(self.tk, value=1, variable=self.condition_var, text='調子が良くなる'), 
                                Radiobutton(self.tk, value=0, variable=self.condition_var, text='変化なし'),
                                Radiobutton(self.tk, value=-1, variable=self.condition_var, text='調子が悪くなる'),]
        self.bonds1_var = IntVar()
        self.bonds1_var.set(0)
        self.bonds1_btns = [Radiobutton(self.tk, value=1, variable=self.bonds1_var),
                            Radiobutton(self.tk, value=2, variable=self.bonds1_var),
                            Radiobutton(self.tk, value=3, variable=self.bonds1_var),
                            Radiobutton(self.tk, value=4, variable=self.bonds1_var),
                            Radiobutton(self.tk, value=0, variable=self.bonds1_var),]
        self.bonds2_var = IntVar()
        self.bonds2_var.set(0)
        self.bonds2_btns = [Radiobutton(self.tk, value=1, variable=self.bonds2_var),
                            Radiobutton(self.tk, value=2, variable=self.bonds2_var),
                            Radiobutton(self.tk, value=3, variable=self.bonds2_var),
                            Radiobutton(self.tk, value=4, variable=self.bonds2_var),
                            Radiobutton(self.tk, value=0, variable=self.bonds2_var),]
        self.bonds3_var = IntVar()
        self.bonds3_var.set(0)
        self.bonds3_btns = [Radiobutton(self.tk, value=1, variable=self.bonds3_var),
                            Radiobutton(self.tk, value=2, variable=self.bonds3_var),
                            Radiobutton(self.tk, value=3, variable=self.bonds3_var),
                            Radiobutton(self.tk, value=4, variable=self.bonds3_var),
                            Radiobutton(self.tk, value=0, variable=self.bonds3_var),]
        self.result = 0
        self.result_text = StringVar()
        self.result_text.set(f'p = {self.result}')
        self.result_label = Label(textvariable=self.result_text)

        self.run_buttton = Button(self.tk, text='計算', command=self.calc_result)

        self.elems = [self.status_entry,
                        self.skill_entry,
                        self.physical_entry,
                        self.traning_btns,
                        self.tips_btns,
                        self.condition_btns,
                        self.bonds1_btns,
                        self.bonds2_btns,
                        self.bonds3_btns,
                        self.result_label,
                        self.run_buttton]

    def setup(self):
        self.tk.geometry(SIZE)
        self.tk.title(TITLE)
        for i in range(len(self.labels)):
            self.labels[i].place(x=PIVOT_LABEL[0], y=PIVOT_LABEL[1]+SEP_LABEL*i)
        
        for i in range(len(self.elems)):
            if type(self.elems[i]) == type(list()):
                if i == INDEX_TRANING:
                    for j in range(len(self.elems[i])):
                        self.elems[i][j].place(x=PIVOT_ELEM[0]+SEP_RADIO_TRANING*j, y=PIVOT_ELEM[1]+SEP_ELEM*i)
                elif i == INDEX_TIPS:
                    for j in range(len(self.elems[i])):
                        self.elems[i][j].place(x=PIVOT_ELEM[0]+SEP_RADIO_TIPS*j, y=PIVOT_ELEM[1]+SEP_ELEM*i)
                elif i == INDEX_CONDITION:
                    for j in range(len(self.elems[i])):
                        self.elems[i][j].place(x=PIVOT_ELEM[0]+SEP_RADIO_CONDITION*j, y=PIVOT_ELEM[1]+SEP_ELEM*i)
                else:
                    for j in range(len(self.elems[i])):
                        self.elems[i][j].place(x=PIVOT_ELEM[0]+SEP_RADIO_BONDS*j, y=PIVOT_ELEM[1]+SEP_ELEM*i)
            else:
                self.elems[i].place(x=PIVOT_ELEM[0], y=PIVOT_ELEM[1]+SEP_ELEM*i)
    
    def run(self):
        self.setup()
        self.tk.mainloop()

    def calc_result(self):
        try:
            up_status = int(self.status_entry.get())
            skill_point = int(self.skill_entry.get())
            physical = int(self.physical_entry.get())
        except ValueError:
            print('不正な値が入力されました')
        self.calc(up_status, skill_point, self.traning_var.get(), self.tips_var.get(), self.condition_var.get(),
                    self.bonds1_var.get(), self.bonds2_var.get(), self.bonds3_var.get(), physical)
        
        self.result_text.set(f'p = {self.result}')

app = P_APP()
app.run()


    