class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert when list is empty
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.ref = new_node  # Point to itself
            self.head = new_node
        else:
            print("List is not empty!")

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.ref = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.ref != self.head:
                temp = temp.ref
            temp.ref = new_node
            new_node.ref = self.head
            self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.ref = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.ref != self.head:
                temp = temp.ref
            temp.ref = new_node
            new_node.ref = self.head

    # Insert at a given position (0-based)
    def insert_position(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            self.insert_begin(data)
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp.ref == self.head:
                print("Position out of bounds")
                return
            temp = temp.ref
        new_node.ref = temp.ref
        temp.ref = new_node

    # Delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        elif self.head.ref == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.ref != self.head:
                temp = temp.ref
            temp.ref = self.head.ref
            self.head = self.head.ref

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.ref == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.ref.ref != self.head:
                temp = temp.ref
            temp.ref = self.head

    # Delete at a given position
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.delete_begin()
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp.ref == self.head:
                print("Position out of bounds")
                return
            temp = temp.ref
        if temp.ref == self.head:
            print("Position out of bounds")
            return
        temp.ref = temp.ref.ref

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.ref
            if temp == self.head:
                break
        print("(head)")

# Example usage:
cll = CircularLinkedList()
cll.insert_empty(10)
cll.insert_begin(5)
cll.insert_end(15)
cll.insert_position(2, 12)
cll.display()  # 5 -> 10 -> 12 -> 15 -> (head)

cll.delete_begin()
cll.display()  # 10 -> 12 -> 15 -> (head)

cll.delete_end()
cll.display()  # 10 -> 12 -> (head)

cll.delete_at_position(1)
cll.display()  # 10 -> (head)