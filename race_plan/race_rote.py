import pandas as pd
from tkinter import *

PATH='race.csv'

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
        self.df_race = pd.read_csv(PATH)
    
    def search_race(self):
        en = self.txt.get()
        s = self.df_race[self.df_race['レース名'].str.contains(en)]
        root = Tk()
        root.title('レース選択')
        root.geometry('500x500')
        print(list(s.iloc[0]))
        print(s.iloc[1])
        root.mainloop()

    def run(self):
        self.tk.mainloop()

race_app = Race_rote_app()
race_app.run()