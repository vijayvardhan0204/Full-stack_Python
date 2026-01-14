class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert when list is empty
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            print("List is not empty!")

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.insert_empty(data)
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            self.head.prev = new_node
            last.next = new_node
            self.head = new_node

    # Insert at end
    def insert_end(self, data):
        if self.head is None:
            self.insert_empty(data)
        else:
            last = self.head.prev
            new_node = Node(data)
            new_node.prev = last
            new_node.next = self.head
            last.next = new_node
            self.head.prev = new_node

    # Insert at a given position (0-based)
    def insert_position(self, pos, data):
        if pos == 0:
            self.insert_begin(data)
            return
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:
                print("Position out of bounds")
                return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    # Delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            last = self.head.prev
            self.head = self.head.next
            self.head.prev = last
            last.next = self.head

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            last = self.head.prev
            second_last = last.prev
            second_last.next = self.head
            self.head.prev = second_last

    # Delete at a given position (0-based)
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.delete_begin()
            return
        temp = self.head
        for _ in range(pos):
            temp = temp.next
            if temp == self.head:
                print("Position out of bounds")
                return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    # Display forward
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage
cdll = CircularDoublyLinkedList()
cdll.insert_empty(10)
cdll.insert_begin(5)
cdll.insert_end(15)
cdll.insert_position(2, 12)
cdll.display()  # 5 <-> 10 <-> 12 <-> 15 <-> (head)

cdll.delete_begin()
cdll.display()  # 10 <-> 12 <-> 15 <-> (head)

cdll.delete_end()
cdll.display()  # 10 <-> 12 <-> (head)

cdll.delete_at_position(1)
cdll.display()  # 10 <-> (head)