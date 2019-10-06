from gui import *


def main():
    tk = Tk()
    tk.geometry("800x450+500+300")
    tk.resizable(False, False)
    app = Engine(tk)
    # app.initUI()

    tk.mainloop()


if __name__ == '__main__':
    main()
