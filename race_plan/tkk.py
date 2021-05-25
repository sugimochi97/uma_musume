from tkinter import *

def btn_click():
    global text, var, bln, chk
    text.set(f'数値:{bln.get()}')
    print(bln.get())
    chk.destroy()

tk = Tk()
tk.title('ウマ娘 p計算ソフト')
tk.geometry('500x400')



txt = Entry(width=20)
txt.place(x=90, y=200)

btn = Button(tk, text='クリック', command=btn_click)
btn.place(x=10, y=10)

bln = BooleanVar()
bln.set(True)

chk = Checkbutton(tk, variable=bln, text="test")
chk.place(x=50, y=70)

t = txt.get()
print(t)

var = IntVar()
var.set(0)

rdo1 = Radiobutton(tk, value=0, variable=var)
rdo1.place(x=70, y=40)

rdo2 = Radiobutton(tk, value=1, variable=var)
rdo2.place(x=70, y=70)

rdo3 = Radiobutton(tk, value=2, variable=var)
rdo3.place(x=70, y=100)

text = StringVar()
text.set(f'数値:{var.get()}')
lbl = Label(textvariable=text)
lbl.place(x=90, y=130)
# canvas.create_polygon(100, 100, 0, 200, 200, 200, outline="red", fill="red")
# canvas.create_text(text='iiiii')

# canvas.pack()
tk.mainloop()