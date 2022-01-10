"""
    ########################
    #   Simple Database    #
    ########################
"""

# make linked list class
class SingleLingkedList:
    class Node:     
        def __init__(self,data,next_node):
            self.data = data 
            self.next = next_node

    def __init__(self,name = None, number = None):
        self.head_name = name
        self.head_number = number

    # inset new item to linked list
    def insert(self,data_name,data_number):
        new_node_name = self.Node(data_name)
        new_node_number = self.Node(data_number)

        if self.head_name == None and self.head_number == None:
            self.head_name = new_node_name
            self.head_number = new_node_number
        else:
            new_node_name.next(self.head_name)
            new_node_number.next(self.head_number)
            
            self.head_name = new_node_name
            self.head_number = new_node_number

    # search some item
    def search(self,data_name,data_number):
        # create current item
        curr_name = self.head_name
        curr_number = self.head_number

        # searching item using looping
        while curr_name == data_name and curr_number == data_number:
            if curr_name.data == data_name and curr_number == data_number:
                result = "Found it"
            else:
                curr_name = curr_name.next
                curr_number = curr_number.next

        return result

    # display all data in linked list
    def show_all_name(self):
        current