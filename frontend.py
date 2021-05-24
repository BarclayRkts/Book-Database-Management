from tkinter import *
import backend as db

class Person:
    def __init__(self, window):
        self.window = window
        self.window.title("Libary Management System")
        self.window.geometry("800x800")


        def addInfo():
            id = 0
            memType = self.member_entry.get()
            bookTitle = self.bookTitle_entry.get()
            firstName = self.firstName_entry.get()
            lastName = self.lastName_entry.get()
            phone = self.phone_entry .get()
            bookID = self.bookID_entry.get()
            author = self.author_entry.get()
            borrowed = self.borrowed_entry.get()
            due = self.due_entry.get()

            data = (id, memType,firstName, lastName, phone, bookID,bookTitle, author, borrowed, due)
            db.insertInfo(data)
            

        MainFrame=Frame(self.window, bg="white")
        MainFrame.grid()  #THIS IS MAIN FRAME OUR WINDOW
        TitleFrame=Frame(MainFrame,bd=1,padx=55,pady=8,bg="black",relief=RIDGE)
        TitleFrame.pack(side=TOP)

        DataFrameRight=LabelFrame(MainFrame,font=('arial',12,'bold'),bd=1,width=450,height=300,bg="Ghost White",relief=RIDGE,text="Book Details\n")
        DataFrameRight.pack(side=BOTTOM, padx=20,pady=20) # This is for Book Details Box
        
        ButtonFrame=Frame(MainFrame,bd=1,width=1350,height=70,padx=18,pady=10,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)#

        DataFrame=Frame(MainFrame,bd=9,width=1300,height=400,padx=20,pady=20,bg="white",relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft=LabelFrame(DataFrame,font=('arial',12,'bold'),padx=20,pady=20, relief=RIDGE,text="Libary Membership Info:\n")
        DataFrameLeft.pack(side=LEFT)


        ##################### Inputs ################################

        self.member_label = Label(DataFrameLeft, text="Membership Type: ", justify=LEFT, anchor="w")
        self.member_label.grid(row=0, column=0)

        self.member_entry = Entry(DataFrameLeft, width=30)
        self.member_entry.grid(row=0, column=1, sticky = W)
        
        self.firstName = Label(DataFrameLeft, text="First Name: ", justify=LEFT, anchor="w")
        self.firstName.grid(row=1, column=0, sticky = W)

        self.firstName_entry = Entry(DataFrameLeft, width=30)
        self.firstName_entry.grid(row=1, column=1)
        
        self.lastName = Label(DataFrameLeft, text="Last Name: ", justify=LEFT, anchor="w")
        self.lastName.grid(row=2, column=0, sticky = W)

        self.lastName_entry = Entry(DataFrameLeft, width=30)
        self.lastName_entry.grid(row=2, column=1)

        self.phone = Label(DataFrameLeft, text="Phone Number: ", justify=LEFT, anchor="w")
        self.phone.grid(row=3, column=0, sticky = W)

        self.phone_entry = Entry(DataFrameLeft, width=30)
        self.phone_entry.grid(row=3, column=1)

        self.bookID = Label(DataFrameLeft, text="Book ID: ", justify=LEFT, anchor="w")
        self.bookID.grid(row=4, column=0, sticky = W)

        self.bookID_entry = Entry(DataFrameLeft, width=30)
        self.bookID_entry.grid(row=4, column=1)

        self.bookTitle = Label(DataFrameLeft, text="Book Title: ", justify=LEFT, anchor="w")
        self.bookTitle.grid(row=5, column=0, sticky = W)

        self.bookTitle_entry = Entry(DataFrameLeft, width=30)
        self.bookTitle_entry.grid(row=5, column=1)

        self.author = Label(DataFrameLeft, text="Author: ", justify=LEFT, anchor="w")
        self.author.grid(row=6, column=0, sticky = W)

        self.author_entry = Entry(DataFrameLeft, width=30)
        self.author_entry.grid(row=6, column=1)

        self.borrowed = Label(DataFrameLeft, text="Date Borrowed: ", justify=LEFT, anchor="w")
        self.borrowed.grid(row=7, column=0, sticky = W)

        self.borrowed_entry = Entry(DataFrameLeft, width=30)
        self.borrowed_entry.grid(row=7, column=1)

        self.due = Label(DataFrameLeft, text="Date Due: ", justify=LEFT, anchor="w")
        self.due.grid(row=8, column=0, sticky = W)

        self.due_entry = Entry(DataFrameLeft, width=30)
        self.due_entry.grid(row=8, column=1)

        ##################### Book Details Box ################################

        bookList=Listbox(DataFrameRight,width=68,height=12,font=('arial',12,'bold'))
        bookList.grid(row=0,column=0,padx=10)
        
        ##################### Buttons ################################
        self.add_btn = Button(ButtonFrame, text="Add Data", width=10, height=2, command=addInfo)
        self.add_btn.grid(row=0, column=0)

        self.display_btn = Button(ButtonFrame, text="Display Data", width=10, height=2)
        self.display_btn.grid(row=0, column=1)

        self.clear_btn = Button(ButtonFrame, text="Clear Data", width=10, height=2)
        self.clear_btn.grid(row=0, column=2)
        
        self.delete_btn = Button(ButtonFrame, text="Delete", width=10, height=2)
        self.delete_btn.grid(row=0, column=3)

        self.update_btn = Button(ButtonFrame, text="Update", width=10, height=2)
        self.update_btn.grid(row=0, column=4)
        
        self.delete_btn = Button(ButtonFrame, text="Search Data", width=10, height=2)
        self.delete_btn.grid(row=0, column=5)

        self.exit_btn = Button(ButtonFrame, text="Exit", width=10, height=2)
        self.exit_btn.grid(row=0, column=6)


if __name__ == '__main__':
    window = Tk()
    app = Person(window)
    window.mainloop()
