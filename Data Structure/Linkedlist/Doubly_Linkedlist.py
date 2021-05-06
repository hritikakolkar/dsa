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
        self.length = 0

    def __len__(self) -> int:
        return self.length
    
    def printlist(self, reverse = False):
        if reverse :
            current_Node = self.tail
            print("None <- ",end="")
            while current_Node.prev != None :
                print(current_Node.data, end=" <-> ")
                current_Node = current_Node.prev
            print(current_Node.data, end=" -> None\n")
        else :
            current_Node = self.head
            print("None <- ",end="")
            while current_Node.next != None :
                print(current_Node.data, end=" <-> ")
                current_Node = current_Node.next
            print(current_Node.data, end=" -> None\n")
            
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
            index = 1
            while index < position :
                current_Node = current_Node.next
                index+=1
            current_Node.next = Node(data = data, next = current_Node.next, prev = current_Node)
            self.length += 1
    
    def remove_First(self) -> None :
        self.head = self.head.next
        self.length -= 1
            
    def remove_Last(self) -> None :
        self.tail = self.tail.prev
        self.length -= 1
           
    def remove(self, position) -> None :
        if position <= 0 :
            self.remove_First()
        elif position >= self.length - 1 :
            self.remove_Last()
        else :
            current_Node = self.head
            index = 0
            while index < position :
                current_Node = current_Node.next
                index += 1
            pass 
            
dllist = Doubly_Linkedlist()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(0)
dllist.insert(100,2)
dllist.printlist()
dllist.printlist(reverse=True)
print(dllist.tail.prev.data)