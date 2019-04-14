from tkinter import *
from logic import *


class Engine(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.place(x=0, y=0, width=800, height=450)

        text_box = Text(wrap=WORD, name="text_box_a")
        text_box2 = Text(wrap=WORD, name="text_box_b")

        btn_exec = Button(self,  # родительское окно
                          text="Find Anagram",  # надпись на кнопке
                          width=20, height=1,  # ширина и высота
                          bg="white", fg="black", command=self.Exec)  # цвет фона и надписи

        # placing
        text_box.place(x=20, y=10, height=25, width=160)
        text_box2.place(x=400, y=10, height=25, width=160)
        btn_exec.place(x=220, y=10)

    def Exec(self):
        print("Action::Calculate")
        text_box = self.parent.nametowidget('text_box_a')
        text_box2 = self.parent.nametowidget('text_box_b')
        text_box2.delete(0.0, END)
        text_box2.insert(0.0, FindAnagram(text_box.get(0.0, END)))

# ================== TIPS ==================== #
# Entry.insert(0, "Saving") only 0 (without dot)
# Text.insert(0.0, "Saving") only 0.0 (with dot)
