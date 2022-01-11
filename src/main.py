"""
    ###########################
    #   Simple Contact App    #
    ###########################
"""

# import some packages
from tkinter import *
from database import SingleLingkedList as SLL

def add_contact():
    add_contact = Tk()

    # make some setting for add contact window
    add_contact.geometry("240x320")
    add_contact.title("Add New Contact")

def main():
    # init main app
    App = Tk()

    # make some setting for main window
    App.geometry("320x400")
    App.title("Contact App")

    # add some widget to window
    search = Entry(width=30,highlightthickness=1)
    search.place(x=38,y=4)
    search.config(highlightbackground="black")

    search_button = Button(text="search")
    search_button.place(x=230, y=0)

    add_button = Button(text="add",command=add_contact)
    add_button.place(x=238,y=100)

    list_label = Label(text="Contact Person")
    list_label.place(x=38,y=110)

    list_contact = Listbox(height=14,width=39,highlightthickness=1)
    list_contact.place(x=38,y=130)

    # intiate object for linked list class
    contact_app_databases = SLL(list_contact)

    contact_app_databases.insert("Daffa",8577)

    clear_button = Button(text="clear")
    clear_button.place(x=38,y=360)

    # start window loop
    App.mainloop()

if __name__ == "__main__":
    main()