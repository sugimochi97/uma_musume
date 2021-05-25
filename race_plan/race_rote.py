import pandas as pd
from tkinter import *
import copy

PATH='race.csv'
SEP=20
CHK_X=10
CHK_Y=10

LIST_X=10
LIST_Y=80

SER_ENT_WIDTH=20
SER_ENT_X=10
SER_ENT_Y=10

MAIN_TITLE='ウマ娘 レース計画ソフト'
MAIN_WINDOW_SIZE='600x500'

SER_BTN_TEXT='検索'
SER_BTN_X=10
SER_BTN_Y=50

UPD_BTN_TEXT = '更新'
UPD_BTN_X=80
UPD_BTN_Y=50

ADD_BTN_TXT='レースを追加'

DONE_RACE = 0


class Race_rote_app():
    def __init__(self):
        self.tk = Tk()
        self.tk.title(MAIN_TITLE)
        self.tk.geometry(MAIN_WINDOW_SIZE)

        self.search_entry = Entry(width=SER_ENT_WIDTH)
        self.search_entry.place(x=SER_ENT_X, y=SER_ENT_Y)

        self.search_btn = Button(self.tk, text=SER_BTN_TEXT, command=self.search_race)
        self.search_btn.place(x=SER_BTN_X, y=SER_BTN_Y)

        self.update_btn = Button(self.tk, text=UPD_BTN_TEXT, command=self.update)
        self.update_btn.place(x=UPD_BTN_X, y=UPD_BTN_Y)

        self.race_list = []

        self.read_race_data()

    def read_race_data(self):
        self.df_race = pd.read_csv(PATH)
    
    def search_race(self):
        self.ent_txt = self.search_entry.get()
        self.search_result = self.df_race[self.df_race['レース名'].str.contains(self.ent_txt)]
        self.search_result = list(self.search_result.itertuples())

        new_window = Toplevel()
        new_window.title('レース選択')
        new_window.geometry('500x500')

        self.search_races = []
        for i in range(len(self.search_result)):
            self.search_races.append(Race(self.search_result[i][2], self.search_result[i][3], self.search_result[i][4], self.search_result[i][5], 
                                        self.search_result[i][6], self.search_result[i][7], self.search_result[i][8], new_window))
            self.search_races[-1].chk.place(x=CHK_X, y=CHK_Y + SEP*i)

        add_btn = Button(new_window, text=ADD_BTN_TXT, command=self.add_race)
        add_btn.place(x=CHK_X, y=CHK_Y + SEP*len(self.search_result))
        new_window.mainloop()
        

    def update(self):
        s = 0
        for i in range(len(self.race_list)):
            if self.race_list[i].bln.get():
                self.race_list[i].chk.destroy()
                self.race_list[i] = DONE_RACE
            else:
                self.race_list[i].chk.place(x=LIST_X, y=LIST_Y + SEP*s)
                s+=1
        
        while DONE_RACE in self.race_list:
            self.race_list.remove(DONE_RACE)
        print([i.name for i in self.race_list])

    def add_race(self):
        for i in range(len(self.search_races)):
            if self.search_races[i].bln.get():
                race = self.search_races[i]
                self.race_list.append(Race(race.year, race.month, race.name, race.race_class, 
                                            race.place, race.length, race.direction, self.tk))
        self.update()

    def run(self):
        self.tk.mainloop()
    
class Race:
    def __init__(self, year, month, name, race_class, place, length, direction, tk):
        self.year = year
        self.month = month
        self.name = name
        self.race_class = race_class
        self.place = place
        self.length = length
        self.direction = direction
        self.bln = BooleanVar()
        self.bln.set(False)
        self.chk = Checkbutton(tk, variable=self.bln, text=self.generate_view_race())


    def generate_view_race(self):
        txt = f'{self.year} {self.month} {self.race_class} {self.name} ' + \
                f'{self.length} {self.place} {self.direction}'
        return txt

race_app = Race_rote_app()
race_app.run()