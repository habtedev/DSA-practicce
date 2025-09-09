class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    

    # remove node at items
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    # Reverse the linkdn list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

# ------------------- Example Usage -------------------

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(10)

print("Original List:")
my_linked_list.print_list()

# Pop first node
removed_node = my_linked_list.pop_first()
print("\nPop First:", removed_node.value)
print("After Pop First:")
my_linked_list.print_list()

# Pop last node
removed_node = my_linked_list.pop()
print("\nPop Last:", removed_node.value)
print("After Pop Last:")
my_linked_list.print_list()

# Prepend a node
my_linked_list.prepend(3)
print("\nAfter Prepend 3:")
my_linked_list.print_list()

# remove
print("\nRemove index 2:", my_linked_list.remove(2))
my_linked_list.print_list()

# reverse
print("\nAfter Reverse:")
my_linked_list.reverse()
my_linked_list.print_list()
