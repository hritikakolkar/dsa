"""
This program is written by Hritik Akolkar
Follow me on Linkedin and Github
"""
# List consists of a number of nodes in which each node has pointer to the following element
# Definig a Node class
class Node:
    """
    Node of Singly Linkedlist
    self.data = data
    self.next = None
    """
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class singlyLinkedlist:
    """
    Operations on a LinkedList
    1) Travesing List
    2) Inserting an item in the list
    3) Deleting an item from the list
    Input : None
    """
    
    def __init__(self, head = Node()) -> None:
        self.head = head
        self.length = 0
    
    def __len__(self) -> int :
        if self.length <=0 : self.length = 0 
        return self.length
        
    def printList(self) -> None :
        current_Node = self.head
        while current_Node != None :
            print(str(current_Node.data),end = "->")
            current_Node = current_Node.next
        print("None")
    
    def prepend(self, data : object) -> None :
        if self.head == None :
            self.head = Node(data = data, next = None)
        else :
            self.head = Node(data = data, next = self.head)
        self.length += 1
    
    def append(self, data : object) -> None :
        if self.head.data == None :
            self.head = Node(data = data, next = None)
        else :
            current_Node = self.head 
            while current_Node.next != None :
                current_Node = current_Node.next
            current_Node.next = Node(data = data , next = None)
            self.length += 1

    def insert(self, position : int, data : object ) -> None :
        if position <= 0 :
            self.append(data)
        elif position >= self.length :
            self.prepend(data)
        else :
            current_Node = self.head
            index = 0
            while index < position :
                current_Node = current_Node.next
                index += 1
            current_Node.next = Node(data= data, next = current_Node.next)
            self.length += 1
    
    def removeFirst(self) -> None :
        self.head = self.head.next
        self.length -= 1
        
    def removeLast(self) -> None :
        pass
    
    def remove(self, position : int) -> None :
        if position <= 0 :
            self.removeFirst()
        elif position >= self.length :
            self.removeLast()
        else :
            current_Node = self.head
            index=1
            while index < position-1:
                current_Node = current_Node.next
                index += 1
            current_Node.next = current_Node.next.next
            self.length -= 1
if __name__ == '__main__':
    #tutorial
    sllist = singlyLinkedlist()
    for number in range(91,92) :
        sllist.append(number)
    sllist.removeFirst()
    sllist.removeLast()
    sllist.remove(position = 4)
    print(len(sllist))
    sllist.printList()    
    
