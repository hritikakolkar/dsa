"""
This program is written by Hritik Akolkar
Follow me on Linkedin and Github
"""
class Node :
    def __init__(self, data : object, next = None) -> None:
        self.data = data
        self.next = next

class Circular_Linkedlist :
    def __init__(self) -> None:
        self.head = Node(data = None , next = None )
        self.tail = self.head
        self.head.next = self.head
        self.length = 1
        
    def print(self) -> None :
        current_Node = self.head 
        while current_Node.next != self.head :
            print(current_Node.data, end = "->")
            current_Node = current_Node.next
        print(current_Node.data)
        
    def append(self, data : object) -> None :
        current_Node = self.head
        while current_Node.next != self.head : 
            current_Node = current_Node.next
        current_Node.next = Node(data = data, next = self.head)
        self.tail = current_Node.next
        self.length += 1
    
    def prepend(self, data : object) -> None :
        self.tail.next = Node(data = data, next = self.head)
        self.length += 1
        
    def insert(self, data : object, position : int ) -> None :
        if position == 0 :
            self.prepend(data = data)
        elif position == self.length - 1 :
            self.append(data = data)
        else :
            current_Node = self.head
            index = 0 
            while current_Node.next != self.head :
                index += 1 
                current_Node = current_Node.next
            current_Node.next = Node(data = data, next = current_Node.next)
            self.length += 1
    