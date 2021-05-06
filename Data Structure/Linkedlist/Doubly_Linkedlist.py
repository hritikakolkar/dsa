"""
This program is written by Hritik Akolkar
Follow me on Linkedin and Github
"""
# Defining Node
class Node :
    def __init__(self, data = None, next = None, prev = None) -> None:
        self.data = data 
        self.next = next
        self.prev = prev

class Doubly_Linkedlist :
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = None

    def __len__(self) -> int:
        return self.length
    
    def append(self, data : object) -> None :
        if self.head == None :
            self.head = Node(data = data)
            self.tail = self.head
        else :
            self.tail.next = Node(data = data, next = None, prev = self.tail)
            self.tail = self.tail.next
        self.length += 1
        
    def prepend(self, data : object) -> None :
        if self.head == None :
            self.head = Node(data = data)
            self.tail = self.head
        else :
            self.head.prev = Node(data = data, next = self.head, prev = None)
            self.head = self.head.prev
        self.length += 1
    
    def insert(self, data : object, position : int ) -> None :
        if position <= 0 :
            self.prepend(data)
        elif position >= self.length - 1:
            self.append(data)
        else :
            current_Node = self.head
            index = 0
            while index < position - 1 :
                current_Node = current_Node.next
            current_Node.next = Node(data = data, next = current_Node.next, prev = current_Node)
            self.length += 1
    