
"""Чистка терминала на случай работы с кодом приложения"""
#import os
#os.system('clear')


import tkinter # Содержит старые элементы управления
import tkinter.ttk # Содержит более новые элементы управления
import tkinter.messagebox # Нужно для вывода окна приложения

class Application(tkinter.ttk.Frame): # Контейнер формирующий содержимое окна приложения (класс производимый от Frame(Простая панель))
    def __init__(self, master=None): # через master конструктору передается ссыка на окно в котором размещается контейнер
        super().__init__(master) # передача окна конструктору суперкласса при его вызове (иначе не заработает)
        self.pack() # Диспетчер компановки (выводит контейнер на экран) 
        self.create_widgets() # Запуск создателя контейнеров
        self.master.title("Motivator") # Замголовок програмы 
        self.master.resizable(False,False) # Пользовательское изменение размеров окна, здесь это не нужно

    def create_widgets(self):
        """Создет контейнеры"""
        self.btnHello = tkinter.ttk.Button(self, text="<<<GET MOTIVATED>>>") # Создание кнопки "HELLO"
        self.btnHello.bind("<ButtonRelease>", self.say_hello) # Событие "<ButtonRelease>" происходит при ОТПУСКАНИИ кнопки мыши и запускается say_hello (Если написать просто <Button> кнопка останется зажатой)
        self.btnHello.pack() # Диспетчер компановки (выводит кнопку на экран(располагает элементы вдоль границ контейнера))
        #               ^pack без параметров поместит кнопку вдоль верхнего края контейнера родителя

        self.btnShow = tkinter.ttk.Button(self) # Создание кнопки "QUIT"
        self.btnShow["text"] = "<<<QUIT>>>" # по сути self.btnShow = tkinter.ttk.Button(self, text="<<<QUIT>>>")
        self.btnShow["command"] = root.destroy # упращенный вариант обработки "шелчка мышью" destroy соотвецтвенно уничтожает окно
        self.btnShow.pack(side="bottom") # Вывод кнопки на экран
        #                  ^ Граница родителя, bottom нижняя граница  

    def say_hello(self, evt): # обработчик события должен принимать единственным параметром экземпляр класса, представляющий обрабатываемое им событие (параметр evt как здесь) 
        tkinter.messagebox.showinfo("Test", "You will succeed!!!") # Вывод сообщения

root = tkinter.Tk() # Tk - главное окно (краеугольный камень приложения)
app = Application(master=root) # Вывод контейнера в главном окне 
root.mainloop() # Запуск приложения, метод класса Тк который запускает цикл обработки      
