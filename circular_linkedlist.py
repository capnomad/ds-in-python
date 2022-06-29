class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CircularLinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = Node(value)
        self.head.next = self.tail
        self.tail.next = self.head

    def is_empty(self):
        return self.head.data is None

    def add(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head

    def display(self):
        current = self.head
        if self.is_empty():
            print("List is empty")
        else:
            print("Nodes in the list are:")
            print(current.data)
            while current.next != self.head:
                current = current.next
                print(current.data)

        
                
cl = CircularLinkedList()

#Adds data to the list    
cl.add(1)   
cl.add(2)    
cl.add(3)    
cl.add(4)  
print(cl)  
#Displays all the nodes present in the list    
cl.display()