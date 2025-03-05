class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        temp = None
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    
    def append_at_first(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def delete(self,pos):
        temp = self.head
        if(pos < 0):
            print("Invalid position")
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        for _ in range(pos):
            if not temp:
                print("Not found")
                return
            temp = temp.next
        if not temp:
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def delete_at_first(self):
        if not self.head:
            print("The list is empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.prev = None

    def delete_at_last(self):
        if not self.head:
            print("THe linked list is empty")
            return
        if not self.head.next:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data,end="<=>")
            current = current.next
        print("None")

ll = linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
ll.append_at_first(90)
ll.display()
ll.delete(1)
ll.display()
ll.delete_at_first()
ll.display()
