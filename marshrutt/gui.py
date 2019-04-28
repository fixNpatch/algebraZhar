import random
from tkinter import *
from tkinter import filedialog, messagebox
from logic import *


class Engine(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.winfo_toplevel().title("Маршрутный ключ")
        self.initUI()

    def initUI(self):
        self.place(x=0, y=0, width=800, height=450)

        text_box = Text(wrap=WORD, name="text_box_q")
        console_box = Text(wrap=WORD, name="console_box_q")
        key_entry = Text(wrap=WORD, name="entry_q")

        btn_open_file = Button(self,  # родительское окно
                               text="Open File",  # надпись на кнопке
                               width=20, height=2,  # ширина и высота
                               bg="white", fg="black", command=self.OpenFile)  # цвет фона и надписи

        btn_save_file = Button(self,
                               text="Save File",
                               width=20, height=2,
                               bg="white", fg="black", command=self.SaveFile)

        btn_clean = Button(self,
                           text="Clean",
                           width=20, height=2,
                           bg="white", fg="black", command=self.CleanTextBox)

        btn_crypt = Button(self,
                           text="Crypt",
                           width=20, height=2,
                           bg="white", fg="black", command=self.Crypt)

        btn_decrypt = Button(self,
                             text="DeCrypt",
                             width=20, height=2,
                             bg="white", fg="black", command=self.DeCrypt)

        # placing
        text_box.place(x=20, y=10, height=100, width=600)
        console_box.place(x=20, y=120, height=310, width=600)
        btn_open_file.place(x=630, y=10)
        btn_save_file.place(x=630, y=60)
        btn_clean.place(x=630, y=110)
        btn_crypt.place(x=630, y=160)
        btn_decrypt.place(x=630, y=210)
        key_entry.place(x=630, y=260, width=150, height=30)

    def OpenFile(self):
        print("Action::OpenFile")
        text_box = self.parent.nametowidget('text_box_q')
        text_box.delete(0.0, END)
        file_path = filedialog.askopenfilename()
        text_box.insert(0.0, open(file_path, "r").read())

    def SaveFile(self):
        print("Action::SaveFile")
        text_box = self.parent.nametowidget('text_box_q')
        flow = open("resources/output.txt", "w+")
        flow.write(text_box.get(0.0, END))
        flow.close()

    def CleanTextBox(self):
        print("Action::Clean")
        text_box = self.parent.nametowidget('text_box_q')
        text_box.delete(0.0, END)

    def Crypt(self):
        print("Action::Crypt")
        key_entry = self.parent.nametowidget('entry_q')
        text_box = self.parent.nametowidget('text_box_q')
        result = MainCrypt(text_box.get(0.0, END), str(key_entry.get(0.0, END)), self)
        text_box.delete(0.0, END)
        text_box.insert(0.0, result)

    def ConsoleLog(self, text):
        console_box = self.parent.nametowidget('console_box_q')
        console_box.insert(END, text)

    def DeCrypt(self):
        print("Action::DeCrypt")
        text_box = self.parent.nametowidget('text_box_q')
        key_entry = self.parent.nametowidget('entry_q')
        result = MainDeCrypt(text_box.get(0.0, END), str(key_entry.get(0.0, END)), self)
        text_box.delete(0.0, END)
        text_box.insert(0.0, result)

# ================== TIPS ==================== #
# Entry.insert(0, "Saving") only 0 (without dot)
# Text.insert(0.0, "Saving") only 0.0 (with dot)
