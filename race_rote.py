import pandas as pd
from tkinter import *

PATH='race.csv'

class Race_rote_app():
    def __init__(self):
        self.tk = Tk()
        self.tk.title('ウマ娘 レース計画ソフト')
        self.tk.geometry('500x400')

        txt = Entry(width=20)
        txt.place(x=90, y=200)

        self.df = pd.read_csv(PATH, index=['a', 'a', 'a', 'a', 'a', 'a', 'a'])
        print(self.df)
            

    def run(self):
        self.tk.mainloop()

race_app = Race_rote_app()
race_app.run()