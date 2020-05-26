# -*- coding: utf-8 -*-

from tkinter import *

def output(event):
    txt = entry1.get()
    
    try:
        if float(txt) < 7:
            label2["text"], label2["bg"] = "Больше", "red"
        elif float(txt) == 7:
            label2["text"], label2["bg"] = "Правильно", "green"
        else:
            label2["text"], label2["bg"] = "Меньше", "red"
    except ValueError:
        label2["text"], label2["bg"] = "Введено не число!!!", "white"            

root = Tk()
root.title("Реши Пример")
root.resizable(False, False)

entry1 = Entry(root, width=5, font=15)
button1 = Button(root, text="Проверить")
label1 = Label(root, width=24, font=15, text="чему равно выражение 2 + 5 = ?")
label2 = Label(root, width=24, font=15)


label1.grid(row=0, columnspan=2) # columnspan определяет сколько колонок занимает контейнер
entry1.grid(row=1, column=0)
button1.grid(row=1, column=1)
label2.grid(columnspan=2)

button1.bind("<Button-1>", output)



root.mainloop()

