"""
    ########################
    #   Simple Database    #
    ########################
"""

# make linked list class
class SingleLingkedList:
    class Node:     
        def __init__(self,data=None,next_node=None):
            self.data = data 
            self.next = next_node

    def __init__(self,name = None, number = None):
        self.head_name = name
        self.head_number = number

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

    # search some item
    def search(self,data_name,data_number):
        # create current item
        curr_name = self.head_name
        curr_number = self.head_number

        # searching item using looping
        while (curr_name != None) and (curr_number != None):
            if (curr_name.data is data_name) and (curr_number.data is data_number):
                print("Found it")

                break
            else:
                curr_name = curr_name.next
                curr_number = curr_number.next

    # display all name data in linked list
    def show_all_name(self):
        curr_name = self.head_name

        while curr_name != None:
            if curr_name.data != None:
                return curr_name.data

            curr_name = curr_name.next

    # display all number data in linked list
    def show_all_number(self):
        curr_number = self.head_number

        while curr_number is not None:
            print(curr_number.data)

            curr_number = curr_number.next
    
    # display both name and number data in linked list
    def show_all(self):
        curr_number = self.head_number

        while curr_number != None:
            print(curr_number.data)

            curr_name = curr_name.next

coba = SingleLingkedList()
coba.insert("daffa",85)
coba.insert("siapa",85)

print(coba.show_all_name())