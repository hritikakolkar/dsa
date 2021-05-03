class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
class Singly_Linkedlist :
    def __init__(self, head : Node ) -> None:
        self.head = head
        self.length = 1