from gui import *


def main():
    tk = Tk()
    tk.geometry("600x80+600+300")
    tk.resizable(False, False)
    app = Engine(tk)
    # app.initUI()

    tk.mainloop()


if __name__ == '__main__':
    main()
