class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node

    def insert_at_position(self,data,pos):
        new_node=Node(data)
        if pos == 1:
            new_node.next=self.head
            self.head=new_node
            return
        curr=self.head
        count=1
        while curr and count < pos-1:
            curr=curr.next
            count+=1
        if curr is None:
            print("position out of range,inserting at end.")
            self.insert_at_end(data)
            return
        new_node.next=curr.next
        curr.next=new_node

    def delete(self,key):
        curr=self.head
        if curr and curr.data==key:
            self.head=curr.next
            return
        prev=None
        while curr and curr.data!=key:
            prev=curr
            curr=curr.next
        if curr:
            prev.next=curr.next
    
    def search(self,key):
        curr=self.head
        while curr:
            if curr.data == key:
                return True
            curr=curr.next
        return False
    
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end=" -> ")
            curr=curr.next
        print("None")

ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(5)

ll.insert_at_position(15, 10)   # insert 15 at position 2

ll.display()
