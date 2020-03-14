class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def length_of_list(self):
        if self.head is None:
            print("List is empty.")
            return

        current_node = self.head
        length = 1
        while current_node.next:
            length += 1
            current_node = current_node.next
        print(length)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("E")
llist.append("D")
# llist.print_list()
llist.insert_after_node(llist.head.next, "C")
llist.print_list()
llist.length_of_list()