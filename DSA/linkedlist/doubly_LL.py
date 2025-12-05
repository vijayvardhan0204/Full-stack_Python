class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Insert at a given position (0-based index)
    def insert_position(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            self.insert_begin(data)
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
        else:
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node

    # Delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None

    # Delete at a given position
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.delete_begin()
            return

        temp = self.head
        for _ in range(pos):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
        else:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next

    # Display forward
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Example usage:
dll = DoublyLinkedList()
dll.insert_empty(10)
dll.insert_begin(5)
dll.insert_end(15)
dll.insert_position(2, 12)  # Insert 12 at position 2
dll.display()               # 5 <-> 10 <-> 12 <-> 15 <-> None

dll.delete_begin()
dll.display()               # 10 <-> 12 <-> 15 <-> None

dll.delete_end()
dll.display()               # 10 <-> 12 <-> None

dll.delete_at_position(1)
dll.display()               # 10 <-> None