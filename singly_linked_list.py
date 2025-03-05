class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def append_at_first(self,data): 
        new_node = Node(data)
        new_node.next =  self.head    
        self.head = new_node
    

    def append_at_any(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def delete_at_first(self):
        if self.head is None:
            print("The linked list is empty")
            return
        self.head = self.head.next

    def delete_at_last(self):
        if not self.head:
            print("The linked list s empty")
            return
        if not self.head.next:
            self.head = None

        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
ll.delete(20)
ll.append(90)
ll.append(55)
ll.display()
ll.delete(10)
ll.append_at_any(555555,2)
ll.display()
ll.append_at_first(500)
ll.display()
ll.delete_at_first()
ll.display()
ll.delete_at_last()
ll.display()