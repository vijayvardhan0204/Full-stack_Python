class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert when list is empty
    def insert_empty(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            print("List is not empty!")

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.ref:
            n = n.ref
        n.ref = new_node

    # Insert at a specific position (0-based index, using your version)
    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head

        if pos == 0:
            np.ref = self.head
            self.head = np
            return

        for _ in range(pos - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.ref
  
        if temp is None:
            print("Position out of bounds")
        else:
            np.ref = temp.ref
            temp.ref = np

    # Delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.ref

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.ref is None:
            self.head = None
            return
        n = self.head
        while n.ref.ref:
            n = n.ref
        n.ref = None

    # Delete at a specific position (0-based index)
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position == 0:
            self.head = self.head.ref
            return
        n = self.head
        for _ in range(position - 1):
            if n is None or n.ref is None:
                print("Position out of bounds")
                return
            n = n.ref
        if n.ref is None:
            print("Position out of bounds")
        else:
            n.ref = n.ref.ref

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while n:
            print(n.data, end=" -> ")
            n = n.ref
        print("None")


# Example usage:
ll = SinglyLinkedList()

ll.insert_empty(10)
ll.insert_begin(5)
ll.insert_end(15)
ll.insert_position(2, 12)  # Insert 12 at position 2
ll.insert_position(3,13)
ll.display()               # 5 -> 10 -> 12 -> 15 -> None

ll.delete_begin()
ll.display()               # 10 -> 12 -> 15 -> None

ll.delete_end()
ll.display()               # 10 -> 12 -> None

ll.delete_at_position(1)
ll.display()               # 10 -> None
















