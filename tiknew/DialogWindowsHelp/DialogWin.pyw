from tkinter import *
from tkinter.messagebox import *

def ask_question_funk(Event):
    answer = askquestion("askquestion", "Окно Первое")
    label1.configure(text=(answer, type(answer)))

def ask_ok_funk(Event):
    answer = askokcancel("askokcancel", "Окно Второе")
    label2.configure(text=(answer, type(answer)))

def ask_yn_funk(Event):
    answer = askyesno("askyesno", "Окно Третье")
    label3.configure(text=(answer, type(answer)))

def ask_rc_funk(Event):
    answer = askretrycancel("askretrycancel", "Окно Четвёртое")
    label4.configure(text=(answer, type(answer)))

def show_info():
    win = Toplevel(root)
    win.title('info')
    info_win = Label(win, text="Программа показывает, какие данные возвращают диалоговые окна (содержание и тип)")
    info_win.pack()


root = Tk()
root.title("Dialog Windows")

main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu)
main_menu.add_cascade(label="INFO", menu=first_item)
first_item.add_command(label="About", command=show_info)

btn1 = Button(root, text="askquestion", font=("Ubuntu", 20), width=12)
btn1.grid(row=0, column=0, sticky="ew")
label1 = Label(root, font=("Ubuntu", 20), width=12)
label1.grid(row=0, column=1)
btn1.bind("<Button-1>", ask_question_funk)

btn2 = Button(root, text="askokcancel", font=("Ubuntu", 20), width=12)
btn2.grid(row=1, column=0, sticky="ew")
label2 = Label(root, font=("Ubuntu", 20), width=12)
label2.grid(row=1, column=1)
btn2.bind("<Button-1>", ask_ok_funk)

btn3 = Button(root, text="askyesno", font=("Ubuntu", 20), width=12)
btn3.grid(row=2, column=0, sticky="ew")
label3 = Label(root, font=("Ubuntu", 20), width=12)
label3.grid(row=2, column=1)
btn3.bind("<Button-1>", ask_yn_funk)

btn4 = Button(root, text="askretrycancel", font=("Ubuntu", 20), width=12)
btn4.grid(row=3, column=0, sticky="ew")
label4 = Label(root, font=("Ubuntu", 20), width=12)
label4.grid(row=3, column=1)
btn4.bind("<Button-1>", ask_rc_funk)

root.mainloop()