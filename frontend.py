from tkinter import *

class Person:
    def __init__(self, window):
        self.window = window
        self.window.title("Libary Management System")
        


if __name__ == '__main__':
    window = Tk()
    app = Person(window)
    window.mainloop()
