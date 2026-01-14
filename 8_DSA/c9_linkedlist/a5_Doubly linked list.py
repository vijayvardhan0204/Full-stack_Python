# Doubly Linked List

# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        """Create a new doubly linked list node."""
        self.data = data
        self.prev = None     # pointer to previous node
        self.next = None     # pointer to next node


class DoublyLinkedList:
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None


    # --------------------------------------------------
    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)

        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return

        # Link new node with current head
        new_node.next = self.head
        self.head.prev = new_node

        # Update head to new node
        self.head = new_node


    # --------------------------------------------------
    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)

        # If empty list
        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        # Move to last node
        while curr.next:
            curr = curr.next

        # Insert new_node after last node
        curr.next = new_node
        new_node.prev = curr


    # --------------------------------------------------
    def insert_at_position(self, data, pos):
        """Insert node at a specific position (1-based index)."""
        new_node = Node(data)

        # Case 1: Insert at position 1
        if pos == 1:
            self.insert_at_beginning(data)
            return

        curr = self.head
        count = 1

        # Move to (pos - 1)-th node
        while curr and count < pos - 1:
            curr = curr.next
            count += 1

        # If position is out of range → insert at end
        if curr is None:
            print("Position out of range, inserting at end.")
            self.insert_at_end(data)
            return

        # Insert in middle
        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:               # If not inserting at end
            curr.next.prev = new_node

        curr.next = new_node


    # --------------------------------------------------
    def delete(self, key):
        """Delete the first node that contains 'key'."""
        curr = self.head

        # Case 1: delete head
        if curr and curr.data == key:
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return

        # Traverse to find key
        while curr and curr.data != key:
            curr = curr.next

        if curr is None:
            print("Value not found.")
            return

        # Case 2: delete in middle or end
        if curr.next:
            curr.next.prev = curr.prev

        curr.prev.next = curr.next


    # --------------------------------------------------
    def search(self, key):
        """Search for a value in the list. Return True/False."""
        curr = self.head

        while curr:
            if curr.data == key:
                return True
            curr = curr.next

        return False


    # --------------------------------------------------
    def display_forward(self):
        """Display list in forward direction."""
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")


    # --------------------------------------------------
    def display_backward(self):
        """Display list in backward direction."""
        curr = self.head

        if curr is None:
            print("None")
            return

        # Move to last node
        while curr.next:
            curr = curr.next

        # Print backward
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None")



# ------------------------
# TESTING THE DLL
# ------------------------
dll = DoublyLinkedList()

dll.insert_at_beginning(20)
dll.insert_at_beginning(10)
dll.insert_at_end(30)
dll.insert_at_position(25, 3)

dll.display_forward()
dll.display_backward()
