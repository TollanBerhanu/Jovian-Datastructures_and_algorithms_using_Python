class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)
    
    def print_values(list):
        current_node = list.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def get_length(self):
        length, current_node = 0, self.head
        while current_node is not None:
            current_node = current_node.next
            length += 1
        return length

    def get_element(self, n):
        current_node = self.head
        i = 1
        while current_node is not None and i < n:
            current_node = current_node.next
            i += 1
        if i == n and current_node is not None:
            return current_node.data
        return None

#a->b->c->d->None
#d->c->b->a->None
#None <- a <- b <- c <- d
def reverse_list(l):
    if l.head is None:
        return
    
    current_node = l.head
    prev_node = None
    
    while current_node is not None:
        # Track the next node
        next_node = current_node.next
        
        # Modify the current node
        current_node.next = prev_node
        
        # Update prev and current
        prev_node = current_node
        current_node = next_node
        
    l.head = prev_node
            
linked_list1 = LinkedList()
linked_list1.append('Node 1')
linked_list1.append('Node 2')
linked_list1.append('Node 3')
linked_list1.append('Node 4')

linked_list1.print_values()
print(linked_list1.get_length())
print(linked_list1.get_element(5))

reverse_list(linked_list1)
linked_list1.print_values()