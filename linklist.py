# Declare the node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList():
    def __init__(self):
        self.head = None

    # Add to the end of thge list
    def append(self, data):
        newNode = Node(data)
        # check if the list is empty
        if not self.head:
           self.head = newNode 
        # if the list is not empty, set the current to the head
        else:
            current = self.head
        # loop the by traversing until the end of the list
            while current.next:
                current = current.next
            current.next = newNode

    # """ Remove from the list """"
    def remove(self, data):
        # check if the data is in the head
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        #Initialise previous to None
        prev = None
        # since the data is not, traverse through the list until we find the node which has the data 
        while current and current.data != data:
            prev = current
            current = current.next
        # the data was not found in the list , we exit
        if not current:
            return
        prev.next = current.next
        current = None

    # Insert into the list using position
    def insert(self, data, position):
        # If the element is in first position as index zero
        
        if position == 0:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

        # if it is not the node in first postion, then we set the heasd has current postiom also declare prev
        else:
            current = self.head 
            prev = None
            for _ in range(position):
                #check if the postion is not out of range
                if not current:
                    return
                # else tranverse through the list until we get to that position 
                prev = current
                current = current.next
            newNode = Node(data)
            newNode.next = current
            prev.next = newNode


    # Delete from the list using postion
    def delete(self, position):
        # Check if the list is not empty
        if not self.head: 
            return
        # if the item is in first position
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None

        for _ in range(position):
            # check if it not out of range
            if not current:
                return
            prev =  current
            current = current.next 
        #Check if it not out of bound  
        if not current:
            return
        prev.next = current.next 
        current = None


    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ->")
            current = current.next
        print(None)


link_list = LinkList()

link_list.append(200)
link_list.append(400)
link_list.append(500)
link_list.append(700)
link_list.append(100)


link_list.insert(300, 0)
link_list.display()
link_list.insert(270, 4)
link_list.display()