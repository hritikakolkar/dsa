"""
This program is written by Hritik Akolkar
Follow me on Linkedin and Github
"""
class Node :
    def __init__(self, data :object, next = None) -> None:
        self.data = data
        self.next = next
class CircularLinkedlist :
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data : object) -> None :
        if self.head == None :
            self.head = Node(data = data, next = None)
            self.head.next = self.head
        else :
            current_Node = self.head
            while current_Node.next != self.head :
                current_Node = current_Node.next
            current_Node.next = Node(data = data, next = self.head)

    def prepend(self, data : object) -> None :
        if self.head == None :
            self.head = Node(data = data, next = None)
            self.head.next = self.head    
        else :
            current_Node = self.head
            while current_Node.next != None :
                current_Node = current_Node.next
            current_Node.next = Node(data = data,next = self.head)
            self.head = current_Node.next
        
    def insert(self, data : object, position : int) -> None :
        if position <= 0 :
            self.prepend()
        elif position >= self.length - 1:
            self.append()
        else:
            current_Node = self.head
            index = 1
            while index < position :
                current_Node = current_Node.next
                index += 1 
            current_Node.next = Node(data = data, next = current_Node.next)
    
    def removeFirst(self) -> None :
        if self.head == None :
            print("Circular Linked list is empty")
        else :
            current_Node = self.head
            while current_Node.next != self.head :
                current_Node = current_Node.next
            self.head = self.head.next
            current_Node.next = self.head

    def removeLast(self) -> None :
        pass
    def remove(self, position : int) -> None :
        pass
    