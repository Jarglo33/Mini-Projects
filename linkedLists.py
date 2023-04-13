class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return "LinkedNode object: Data = {0}, Next = {1}".format(self.data, self.next)
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node

class DoubleLinkedNode(LinkedNode):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None
    
    def __repr__(self) -> str:
        return "LinkedNode object: Data = {0}, Next = {1}".format(self.data,self.next)
    
    def get_previous(self):
        return self.previous
    
    def set_previous(self, previous_node):
        self.previous = previous_node
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self) -> str:
        return "LinkedList object: Head = {0}".format(self.head)
    
    def is_empty(self):
        return self.head is None
    
    def append_head(self, data):
        old_node = self.head
        self.head = LinkedNode(data)
        self.head.set_next(old_node)

    def size(self):
        if self.head is None:
            return 0
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size
    
    def search(self, data):
        if self.head is None:
            return "Linked List is empty. please add data"
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False
        
    
    def remove(self, data):
        if self.head is None:
            return "Linked List is empty. please add data"
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == data:
                break
            else:
                if current.get_next() is None:
                    return f"{data} is not in this Linked List"
                else:
                    previous = current
                    current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return f"Succesfully removed {data}"
                    
class DoubleLinkedList(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self) -> str:
        return "DoubleLinkedList object: \nHead = {0}\n\nTail = {1}".format(self.head,self.tail)
    
    def get_end(self):
        return self.tail
    
    def append_head(self, data):
        old_node = self.head
        self.head = DoubleLinkedNode(data)
        self.head.set_next(old_node)
        if old_node == None:
            self.tail = self.head
        else:
            old_node.set_previous(self.head)
    
    
    def append_tail(self, data):
        old_node = self.tail
        self.tail = DoubleLinkedNode(data)
        self.tail.set_previous(old_node)
        if old_node == None:
            self.head = self.tail
        else:
            old_node.set_next(self.tail)
    
    def search(self, data):
        if self.head is None:
            return "Double Linked List is empty. please add data"
        if self.tail.get_data() == data:
            return True
        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False
        
    def reverse_search(self, data):
        if self.head is None:
            return "Double Linked List is empty. please add data"
        if self.head.get_data() == data:
            return True
        current = self.tail
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_previous()
        return False
    
    def remove(self, data):
        skip = False
        if self.head is None:
            return "Double Linked List is empty. please add data"
        current = self.head
        previous = None
        next_node = self.head.get_next()
        
        while current is not None and not skip:
            if current.get_data() == data:
                break
            else:
                if current.get_next() is None:
                    return f"{data} is not in this Double Linked List"
                else:
                    previous = current
                    current = current.get_next()
                    next_node = current.get_next()
                    
        if previous == None:
            self.head = current.get_next()
            self.head.set_previous(None)
        elif next_node == None:
            self.tail = current.get_previous()
            self.tail.set_next(None)
        else:
            next_node.set_previous(previous)
            previous.set_next(current.get_next())
        return f"Succesfully removed {data}"

def test_linked_list():
    #Head to Tail test
    ll = LinkedList()
    string = "Jarren Glover"
    for i in range(len(string)-1, -1,-1):
        ll.append_head(string[i])

    print(ll.is_empty())
    print(ll.size())
    print(ll.search("l"))
    print(ll.remove("l"))
    print(ll.size())
    print(ll.search("l"))
    print(ll.remove("l"))

def test_double_linked_list():
    #Head to Tail test
    dll = DoubleLinkedList()
    string = "Jarren Glover"
    for i in range(len(string)-1, -1,-1):
        dll.append_head(string[i])

    print(dll.is_empty())
    print(dll.size())
    print(dll.search("l"))
    print(dll.get_end())
    print(dll.remove("l"))
    print(dll.size())
    print(dll.search("l"))
    print(dll.remove("l"))
    
    print('\n\n\n')
    
    #Tail to Head test
    dll = DoubleLinkedList()
    string = "Jarren Glover"
    for i in range(len(string)-1, -1,-1):
        dll.append_tail(string[i])

    print(dll.is_empty())
    print(dll.size())
    print(dll.reverse_search("l"))
    print(dll.get_end())
    print(dll.remove("l"))
    print(dll.size())
    print(dll.reverse_search("l"))
    print(dll.remove("l"))
