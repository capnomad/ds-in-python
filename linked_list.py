class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        return ' -> '.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def add_node(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = Node(value)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
def main():
    try:
        ll = LinkedList()
        while True:
            print("\nEnter a number:", end=" ")
            new_node = input()
            ll.add_node(int(new_node))
            print("Linked List: ",ll)
            print("Length: ", len(ll))
    except ValueError:
        print("Final Linked list: ", ll)
        print("Wrong input, Exiting now!!!")
        exit(0)

if __name__=="__main__":
    main()
