import tkinter
import tkinter.ttk
"""Скрипт Python запускающий несколько окон
Редактирование кода позволяет оставить активными как все окна, так и только «Верхнее» """

class Secondary (tkinter.ttk.Frame):
    def __init__(self, master=None, parent=None):
        super().__init__(master)
        self.parent = parent
        self.pack()
        self.create_widgets()
        self.master.title("Вторичное окно")
        self.master.resizable(False, False)
        self.focus_set()
        self.master.transient(parent)
        self.grab_set()

    def create_widgets(self):
        self.varValue = tkinter.StringVar()
        self.varValue.set("Значение")

        entValue = tkinter.ttk.Entry(self, textvariable=self.varValue)
        entValue.pack()

        #btnShow = tkinter.ttk.Button(self, text="Вывести значение", command=self.show_value)
        #btnShow.pack()

#    def show_value(self):
#        self.parent.lblValue["text"] = self.varValue.get()
     
        btnOK = tkinter.ttk.Button(self, text="OK", command=self.ok)
        btnOK.pack(side="left")

        btnCancel = tkinter.ttk.Button(self, text="Отмена", command=self.master.destroy)
        btnCancel.pack(side="right")

    def ok(self):
        self.parent.lblValue["text"] = self.varValue.get()
        self.master.destroy()    


class Application(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master.title("Обычные вторичные окна")
        self.master.resizable(False, False)

    def create_widgets(self):
        btnShow = tkinter.ttk.Button(self, text="Вывести окно", command=self.show_window)
        btnShow.pack()

        self.lblValue = tkinter.ttk.Label(self, text="0", width=50)
        self.lblValue.pack()

    def show_window(self):
        Secondary(master=tkinter.Toplevel(), parent=self)

root = tkinter.Tk()
app = Application(master=root)
root.mainloop()            



