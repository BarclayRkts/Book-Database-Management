from os import set_blocking
from tkinter import *
from tkinter import messagebox
import backend as db

class Person:
    def __init__(self, window):
        self.window = window
        self.window.title("Libary Management System")
        self.window.geometry("1000x800")


        def addInfo():
            id = 0
            memType = clicked.get()
            bookTitle = self.bookTitle_entry.get()
            firstName = self.firstName_entry.get()
            lastName = self.lastName_entry.get()
            phone = self.phone_entry .get()
            bookID = self.bookID_entry.get()
            author = self.author_entry.get()
            borrowed = self.borrowed_entry.get()
            due = self.due_entry.get()

            data = (id, memType,firstName, lastName, phone, bookID,bookTitle, author, borrowed, due)

            insertion = db.insertInfo(data)
            
            if insertion != 1:
                messagebox.showinfo("Libary Management System", "Data Entered Successfully")
            else:
                messagebox.showinfo("Libary Management System", "Something Went Wrong. Try Again!")
            
            display()
            
        def display():
            results = db.displayInfo()
            bookList.delete(0,END)

            for row in results:
                bookList.insert(END, row)

        def clear():
            # clicked.get().delete(0, END)
            self.bookTitle_entry.delete(0, END)
            self.firstName_entry.delete(0, END)
            self.lastName_entry.delete(0, END)
            self.phone_entry .delete(0, END)
            self.bookID_entry.delete(0, END)
            self.author_entry.delete(0, END)
            self.borrowed_entry.delete(0, END)
            self.due_entry.delete(0, END)
        
        def selectedBox(event):
            global sb 
            #clickedBook = bookList.get(ANCHOR)
            clickedBook = bookList.curselection()[0]
            sb = bookList.get(clickedBook)
            
            self.firstName_entry.delete(0, END)
            self.firstName_entry.insert(END, sb[1])
            
            self.lastName_entry.delete(0, END)
            self.lastName_entry.insert(END, sb[2])

            self.phone_entry.delete(0, END)
            self.phone_entry.insert(END, sb[3])
            
            self.bookID_entry.delete(0, END)
            self.bookID_entry.insert(END, sb[4])

            self.bookTitle_entry.delete(0, END)
            self.bookTitle_entry.insert(END, sb[5])

            self.author_entry.delete(0, END)
            self.author_entry.insert(END, sb[6])

            self.borrowed_entry.delete(0, END)
            self.borrowed_entry.insert(END, sb[7])

            self.due_entry.delete(0, END)
            self.due_entry.insert(END, sb[8])
            
            print(sb)

        def exit():
            window.destroy()

        MainFrame=Frame(self.window, bg="white")
        MainFrame.grid()

        DetailsFrame=LabelFrame(MainFrame,font=('arial',12,'bold'),bd=1,width=450,height=300,bg="Ghost White",relief=RIDGE,text="Book Details\n")
        DetailsFrame.pack(side=BOTTOM, padx=20,pady=20) # This is for Book Details Box
        
        ButtonFrame=Frame(MainFrame,bd=1,width=1350,height=70,padx=18,pady=10,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=9,width=1300,height=400,padx=20,pady=20,bg="white",relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        InputFrame=LabelFrame(DataFrame,font=('arial',12,'bold'),padx=20,pady=20, relief=RIDGE,text="Libary Membership Info:\n")
        InputFrame.pack(side=LEFT)


        ##################### Inputs ################################

        self.member_label = Label(InputFrame, text="Membership Type: ", justify=LEFT, anchor="w")
        self.member_label.grid(row=0, column=0)

        clicked = StringVar()
        clicked.set("         ")
        self.drop = OptionMenu(InputFrame, clicked, "Administrator", "Staff", "Student")
        self.drop.config(width=25, bg="white", justify=LEFT, anchor="w")
        self.drop.grid(row=0, column=1, sticky = W)
        
        self.firstName = Label(InputFrame, text="First Name: ", justify=LEFT, anchor="w")
        self.firstName.grid(row=1, column=0, sticky = W)

        self.firstName_entry = Entry(InputFrame, width=30)
        self.firstName_entry.grid(row=1, column=1)
        
        self.lastName = Label(InputFrame, text="Last Name: ", justify=LEFT, anchor="w")
        self.lastName.grid(row=2, column=0, sticky = W)

        self.lastName_entry = Entry(InputFrame, width=30)
        self.lastName_entry.grid(row=2, column=1)

        self.phone = Label(InputFrame, text="Phone Number: ", justify=LEFT, anchor="w")
        self.phone.grid(row=3, column=0, sticky = W)

        self.phone_entry = Entry(InputFrame, width=30)
        self.phone_entry.grid(row=3, column=1)

        self.bookID = Label(InputFrame, text="Book ID: ", justify=LEFT, anchor="w")
        self.bookID.grid(row=4, column=0, sticky = W)

        self.bookID_entry = Entry(InputFrame, width=30)
        self.bookID_entry.grid(row=4, column=1)

        self.bookTitle = Label(InputFrame, text="Book Title: ", justify=LEFT, anchor="w")
        self.bookTitle.grid(row=5, column=0, sticky = W)

        self.bookTitle_entry = Entry(InputFrame, width=30)
        self.bookTitle_entry.grid(row=5, column=1)

        self.author = Label(InputFrame, text="Author: ", justify=LEFT, anchor="w")
        self.author.grid(row=6, column=0, sticky = W)

        self.author_entry = Entry(InputFrame, width=30)
        self.author_entry.grid(row=6, column=1)

        self.borrowed = Label(InputFrame, text="Date Borrowed: ", justify=LEFT, anchor="w")
        self.borrowed.grid(row=7, column=0, sticky = W)

        self.borrowed_entry = Entry(InputFrame, width=30)
        self.borrowed_entry.grid(row=7, column=1)

        self.due = Label(InputFrame, text="Date Due: ", justify=LEFT, anchor="w")
        self.due.grid(row=8, column=0, sticky = W)

        self.due_entry = Entry(InputFrame, width=30)
        self.due_entry.grid(row=8, column=1)

        ##################### Book Details Box ################################

        bookList=Listbox(DetailsFrame,width=100,height=12,font=('arial',12,'bold'))
        bookList.bind('<<ListboxSelect>>', selectedBox)
        bookList.grid(row=0,column=0,padx=10)
        
        
        ##################### Buttons ################################
        self.add_btn = Button(ButtonFrame, text="Add Data", width=10, height=2, command=addInfo)
        self.add_btn.grid(row=0, column=0)

        self.display_btn = Button(ButtonFrame, text="Display Data", width=10, height=2, command=display)
        self.display_btn.grid(row=0, column=1)

        self.clear_btn = Button(ButtonFrame, text="Clear Data", width=10, height=2, command=clear)
        self.clear_btn.grid(row=0, column=2)

        self.exit_btn = Button(ButtonFrame, text="Exit", width=10, height=2, command=exit)
        self.exit_btn.grid(row=0, column=6)

if __name__ == '__main__':
    window = Tk()
    app = Person(window)
    window.mainloop()
