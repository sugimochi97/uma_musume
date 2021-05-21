import csv
import pandas as pd
from tkinter import *

PATH='race.csv'
RACE_COLUMNS = ['年', '月', 'レース名', 'クラス', '場所', '距離', '回り']

class Race_rote_app():
    def __init__(self):
        self.tk = Tk()
        self.tk.title('ウマ娘 レース計画ソフト')
        self.tk.geometry('600x500')

        self.txt = Entry(width=20)
        self.txt.place(x=10, y=10)

        btn = Button(self.tk, text='検索', command=self.search_race)
        btn.place(x=10, y=50)

        self.text = StringVar()
        self.text.set('')
        self.label = Label(textvariable=self.text)
        self.label.place(x=10, y=80)

        self.read_race_data()

    def read_race_data(self):
        self.df_race = pd.read_csv(PATH, names=RACE_COLUMNS)
    
    def search_race(self):
        en = self.txt.get()
        s = self.df_race[self.df_race['レース名'].str.contains(en)]
        self.text.set(s)

    def run(self):
        self.tk.mainloop()

race_app = Race_rote_app()
race_app.run()