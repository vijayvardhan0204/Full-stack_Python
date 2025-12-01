# Node class represents one element in the linked list
class Node:
    def __init__(self, data):
        self.data = data       # store value
        self.next = None       # pointer to next node (initially empty)

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None       # initially linked list is empty

    # Insert a value at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)          # create new node
        new_node.next = self.head      # point new node to current head
        self.head = new_node           # make new node the head

    # Insert a value at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return

        curr = self.head               # start from head

        # Move until reaching last node (node whose next is None)
        while curr.next:
            curr = curr.next

        curr.next = new_node           # attach new node at the end

    # Insert node at a specific position (1-based index)
    def insert_at_position(self, data, pos):
        new_node = Node(data)

        # If inserting at position 1 → same as insert_at_beginning
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        count = 1

        # Traverse until reaching (pos - 1)th node
        while curr and count < pos - 1:
            curr = curr.next
            count += 1

        # If position is out of range, insert at end
        if curr is None:
            print("Position out of range, inserting at end.")
            self.insert_at_end(data)
            return

        # Insert new node between curr and curr.next
        new_node.next = curr.next
        curr.next = new_node

    # Delete a node with a specific key (value)
    def delete(self, key):
        curr = self.head

        # Case 1: key is at head
        if curr and curr.data == key:
            self.head = curr.next
            return

        prev = None

        # Traverse list until key is found
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        # If key is found, delete it by skipping the node
        if curr:
            prev.next = curr.next

    # Search for a value in linked list
    def search(self, key):
        curr = self.head

        # Traverse through each node
        while curr:
            if curr.data == key:
                return True       # key found
            curr = curr.next
        return False               # not found

    # Display the entire linked list
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")             # marks the end of list


# ------------------ TESTING THE LINKED LIST ------------------

ll = LinkedList()

ll.insert_at_beginning(10)   # list: 10
ll.insert_at_beginning(20)   # list: 20 -> 10
ll.insert_at_end(5)          # list: 20 -> 10 -> 5

ll.insert_at_position(15, 10)  # position out of range → insert at end

ll.display()  # Output: 20 -> 10 -> 5 -> 15 -> None
