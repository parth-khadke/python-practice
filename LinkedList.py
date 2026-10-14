class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head 
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
   
    def insert_in_position(self, data, pos):
        new_node = Node(data)
        
        if pos ==1:
            self.insert_at_beginning(data)
            return
        
        current = self.head
        count = 1
        while current is not None and count < pos - 1:
            current = current.next
            count+=1
        
        if current is None:
            print("Position is out of range.")
            return
        
        new_node.next = current.next
        current.next = new_node
        
        if new_node.next is None:
            self.tail = new_node 
        
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head == self.tail:
            self.head , self.tail = None
            return
        
        current = self.head
        
        while current.next != self.tail:
            current = current.next 
            
        self.tail = current
        current.next = None
        

ll = LinkedList()


ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.insert_at_end(60)

ll.delete_at_end()
ll.delete_at_end()

ll.traverse()
