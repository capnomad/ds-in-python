class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.value)


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        return u"\u2022" + " <- (head) "+' <--> '.join([str(node) for node in self])+" (tail) -> "+ u"\u2022"

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def add_at_head(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            node = Node(value=value, next=self.head, prev=None)
            self.head.prev = node
            self.head = node

    def add_at_tail(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            node = Node(value=value, next = None, prev=self.tail)
            self.tail.next = node
            self.tail = node

    def is_empty(self):
        return self.__len__() == 0

def main():
    try:
        ll = DoublyLinkedList()
        print("Empty?: ", ll.is_empty())
        while True:
            print("\nEnter a number:", end=" ")
            new_node = input()
            ll.add_at_head(int(new_node))
            print("Linked List: ",ll)
            print("Length: ", len(ll))
    except (ValueError, KeyboardInterrupt):
        ll.add_at_tail(-1)
        ll.add_at_tail(-2)
        ll.add_at_tail(-3)
        ll.add_at_tail(-4)
        print("Final Linked list: ", ll)
        print("Empty?: ", ll.is_empty())
        print("Total Items", len(ll))
        print("Wrong input, Exiting now!!!")
        exit(0)

if __name__=="__main__":
    main()
