"""
    ###########################
    #   Simple Contact App    #
    ###########################
"""

# import some packages
from tkinter import *

class ContactApp:
    # make class node to save value
    class Node:     
        def __init__(self,data=None,next_node=None):
            # init data and next for data
            self.data = data 
            self.next = next_node

    def __init__(self,name = None, number = None):
        # init head for node in linked list
        self.head_name = name
        self.head_number = number

        # init main app
        self.App = Tk()

        # make some setting for main window
        self.App.geometry("320x400")
        self.App.title("Contact App")

        
    # inset new item to linked list at the end
    def insert(self,data_name,data_number):
        # create both number and name new node
        new_node_name = self.Node(data_name)
        new_node_number = self.Node(data_number)
        
        if (self.head_name is None) and (self.head_number is None):
            # add new node to first node if first node empty
            self.head_name = new_node_name
            self.head_number = new_node_number
        else:
            # add to next node after first node
            last_name = self.head_name
            last_number = self.head_number

            while (last_name.next) and (last_number.next):
                last_name = last_name.next
                last_number = last_number.next

            # add new insert node value
            last_name.next = new_node_name
            last_number.next = new_node_number

    # display all name data in linked list
    def show_all_name(self,list_box):
        curr_name = self.head_name

        while curr_name != None:
            list_box.insert(curr_name.data)

            curr_name = curr_name.next

    # make add contact function
    def add_contact(self):
        # init contact window
        self.add_contact_window = Tk()

        # make some setting for add contact window
        self.add_contact_window.geometry("240x320")
        self.add_contact_window.title("Add New")


        # make some layout here
        name_label = Label(self.add_contact_window,text="Name: ")
        name_label.place(x=15,y=15)

        name_entry = Entry(self.add_contact_window,width=32,highlightthickness=1)
        name_entry.place(x=17,y=34)

        number_label = Label(self.add_contact_window,text="Phone Number: ")
        number_label.place(x=15,y=62)

        number_entry = Entry(self.add_contact_window,width=32,highlightthickness=1)
        number_entry.place(x=17,y=81)

        add_button = Button(self.add_contact_window,text="Add Contact")
        add_button.place(x=60,y=135)

        def insert_new_contact():
            number_entry.g
        

    def main(self):
        # add some widget to window
        search = Entry(self.App,width=30,highlightthickness=1)
        search.place(x=38,y=4)
        search.config(highlightbackground="black")

        search_button = Button(self.App,text="search")
        search_button.place(x=230, y=0)

        add_button = Button(self.App,text="add",command=self.add_contact)
        add_button.place(x=238,y=100)

        list_label = Label(self.App,text="Contact Person")
        list_label.place(x=38,y=110)

        list_contact = Listbox(self.App,height=14,width=39,highlightthickness=1)
        list_contact.place(x=38,y=130)

        clear_button = Button(self.App,text="clear")
        clear_button.place(x=38,y=360)

        # start window loop
        self.App.mainloop()

start_app = ContactApp()

start_app.main()