from tkinter import *
from tkinter import filedialog, messagebox
from logic import *

class Test(Text):
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        self.bind('<Control-c>', self.copy)
        self.bind('<Control-x>', self.cut)
        self.bind('<Control-v>', self.paste)

    def copy(self):
        self.clipboard_clear()
        text = self.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)

class Engine(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.winfo_toplevel().title("Проверка множества")
        self.initUI()
        self.PATH = ""

    def initUI(self):
        self.place(x=0, y=0, width=800, height=450)

        console_box = Text(self.parent, wrap=WORD, name="console_box_q")

        btn_open_file = Button(self,  # родительское окно
                               text="Open File",  # надпись на кнопке
                               width=20, height=2,  # ширина и высота
                               bg="white", fg="black", command=self.OpenFile)  # цвет фона и надписи

        btn_clean_console = Button(self,
                           text="CleanConsole",
                           width=20, height=2,
                           bg="white", fg="black", command=self.CleanConsoleBox)

        btn_check = Button(self,
                           text="Check",
                           width=20, height=2,
                           bg="white", fg="black", command=self.Check)


        # placing
        console_box.place(x=20, y=70, height=350, width=750)
        btn_open_file.place(x=20, y=10)
        btn_clean_console.place(x=200, y=10)
        btn_check.place(x=380, y=10)

    def OpenFile(self):
        print("Action::OpenFile")
        file_path = filedialog.askopenfilename()
        self.PATH = file_path
        print("file opened::source is below")
        print(self.PATH)

    def CleanConsoleBox(self):
        print("Action::CleanConsole")
        console_box = self.parent.nametowidget('console_box_q')
        console_box.delete(0.0, END)

    def Check(self):
        print("Action::Check")
        console_box_q = self.parent.nametowidget('console_box_q')
        result = MainCheck(self.PATH, self)
        console_box_q.insert(END, result)

    def ConsoleLog(self, text):
        console_box = self.parent.nametowidget('console_box_q')
        console_box.insert(END, text)


# ================== TIPS ==================== #
# Entry.insert(0, "Saving") only 0 (without dot)
# Text.insert(0.0, "Saving") only 0.0 (with dot)
