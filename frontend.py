from tkinter import *

class Person:
    def __init__(self, window):
        self.window = window
        self.window.title("Libary Management System")
        self.window.geometry("1300x1000")
        
        # self.title_label = Label(
        #                     window, 
        #                     text="Libary Database Management System", 
        #                     background='black',
        #                     font=('Futura', 32),
        #                     fg='white',
        #                     width=55,
        #                     height=2)
        # self.title_label.grid(row=0, column=0, sticky=('N', 'S', 'E', 'W'), padx=5, pady=10)

        MainFrame=Frame(self.window, bg="white")
        MainFrame.grid()  #THIS IS MAIN FRAME OUR WINDOW
        TitleFrame=Frame(MainFrame,bd=1,padx=55,pady=8,bg="black",relief=RIDGE)
        TitleFrame.pack(side=TOP)#THIS IS STITLE FRAME
        
        DataFrame=Frame(MainFrame,bd=9,width=1300,height=400,padx=20,pady=20,bg="white",relief=RIDGE)
        DataFrame.pack(side=BOTTOM)#THIS IS STI

        DataFrameLeft=LabelFrame(DataFrame,font=('arial',12,'bold'),relief=RIDGE,text="Libary Membership Info:\n")
        DataFrameLeft.pack(side=LEFT)

        ##################### Inputs ################################

        self.member_label = Label(DataFrameLeft, text="Membership Type: ", justify=LEFT, anchor="w")
        self.member_label.grid(row=0, column=0)

        self.member_entry = Entry(DataFrameLeft, width=30)
        self.member_entry.grid(row=0, column=1, sticky = W)

        self.title_label = Label(DataFrameLeft, text="Title: ", justify=LEFT, anchor="w")
        self.title_label.grid(row=1, column=0, sticky = W)

        self.title_entry = Entry(DataFrameLeft, width=30)
        self.title_entry.grid(row=1, column=1)
        
        self.firstName = Label(DataFrameLeft, text="First Name: ", justify=LEFT, anchor="w")
        self.firstName.grid(row=2, column=0, sticky = W)

        self.firstName_entry = Entry(DataFrameLeft, width=30)
        self.firstName_entry.grid(row=2, column=1)
        
        self.lastName = Label(DataFrameLeft, text="Last Name: ", justify=LEFT, anchor="w")
        self.lastName.grid(row=3, column=0, sticky = W)

        self.lastName_entry = Entry(DataFrameLeft, width=30)
        self.lastName_entry.grid(row=3, column=1)

        self.lastName = Label(DataFrameLeft, text="Last Name: ", justify=LEFT, anchor="w")
        self.lastName.grid(row=4, column=0, sticky = W)

        self.lastName_entry = Entry(DataFrameLeft, width=30)
        self.lastName_entry.grid(row=4, column=1)

        self.phone = Label(DataFrameLeft, text="Phone Number: ", justify=LEFT, anchor="w")
        self.phone.grid(row=5, column=0, sticky = W)

        self.phone_entry = Entry(DataFrameLeft, width=30)
        self.phone_entry.grid(row=5, column=1)

        self.bookID = Label(DataFrameLeft, text="Book ID: ", justify=LEFT, anchor="w")
        self.bookID.grid(row=6, column=0, sticky = W)

        self.bookID_entry = Entry(DataFrameLeft, width=30)
        self.bookID_entry.grid(row=6, column=1)

        self.bookTitle = Label(DataFrameLeft, text="Book Title: ", justify=LEFT, anchor="w")
        self.bookTitle.grid(row=7, column=0, sticky = W)

        self.bookTitle_entry = Entry(DataFrameLeft, width=30)
        self.bookTitle_entry.grid(row=7, column=1)

        self.author = Label(DataFrameLeft, text="Author: ", justify=LEFT, anchor="w")
        self.author.grid(row=8, column=0, sticky = W)

        self.author_entry = Entry(DataFrameLeft, width=30)
        self.author_entry.grid(row=8, column=1)

        self.borrowed = Label(DataFrameLeft, text="Date Borrowed: ", justify=LEFT, anchor="w")
        self.borrowed.grid(row=9, column=0, sticky = W)

        self.borrowed_entry = Entry(DataFrameLeft, width=30)
        self.borrowed_entry.grid(row=9, column=1)

        self.due = Label(DataFrameLeft, text="Date Due: ", justify=LEFT, anchor="w")
        self.due.grid(row=10, column=0, sticky = W)

        self.due_entry = Entry(DataFrameLeft, width=30)
        self.due_entry.grid(row=10, column=1)



        


if __name__ == '__main__':
    window = Tk()
    app = Person(window)
    window.mainloop()
