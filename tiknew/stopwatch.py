# -*- coding: utf-8 -*-

"""Импорт нужных модулей"""
from os import system 
system('clear') # Для чистки консоли
from tkinter import * # Для отрисовки
from datetime import datetime # Для расчета секунд

sec = 0 # Переменная отсчета секунд
Wtime = 0 # Переменная времени

def step():
    """Шаги таймера"""
    global sec, Wtime
    Wtime = root.after(1000, step) # Запись пройденных секунд
    label1.configure(text=str(datetime.fromtimestamp(sec).strftime("%M:%S")))
    sec += 1

def start_sw():
    """Нажатие кнопки START"""
    start_bt.grid_forget() # grid_forget скрывает кнопку
    stop_bt.grid(row=1, columnspan=2, sticky="ew") # grid отрисоввывает кнопку
    step() # запуск функции step()

def stop_sw():
    """Нажатие кнопки STOP"""
    stop_bt.grid_forget()
    cont_bt.grid(row=1, column=0, sticky="ew")
    cls_bt.grid(row=1, column=1, sticky="ew")
    root.after_cancel(Wtime) # фиксирует пройденные секунды

def continue_sw():
    """Нажатие клавиши CONTINUE"""
    cont_bt.grid_forget()
    cls_bt.grid_forget()
    stop_bt.grid(row=1, columnspan=2, sticky="ew")
    step()

def clear_sw():
    """Очистка секундомера"""
    global sec
    sec = 0
    label1.configure(text="00:00") # Возврат в изначальное состояние
    cont_bt.grid_forget()
    cls_bt.grid_forget()
    start_bt.grid(row=1, columnspan=2, sticky="ew")

root = Tk()
root.title("WATCH")

"""Отрисовка окна"""
label1 = Label(root, width=5, font = ("Arial", 100), text="00:00")
label1.grid(row=0, columnspan=2)

"""Поведение кнопок"""
start_bt = Button(root, text="START", font=("Arial", 30), command=start_sw)
stop_bt = Button(root, text="STOP", font=("Arial", 30), command=stop_sw)
cont_bt = Button(root, text="CONTINUE", font=("Arial", 30), command=continue_sw)
cls_bt = Button(root, text="CLEAR", font=("Arial", 30), command=clear_sw)

start_bt.grid(row=1, columnspan=2, sticky="ew") # Первая кнопка на экране

root.mainloop()

