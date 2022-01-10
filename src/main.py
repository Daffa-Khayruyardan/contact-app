"""
    ###########################
    #   Simple Contact App    #
    ###########################
"""
# import some packages
from tkinter import *

def main():
    # init main app
    App = Tk()

    # set window size
    App.geometry("320x400")

    # set app title
    App.title("Contact App")

    # add background color
    App.configure(bg='#3D454E')

    # add some search textbox
    search = Entry(App, width=30)
    search.pack()

    App.mainloop()

if __name__ == "__main__":
    main()