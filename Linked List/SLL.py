class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_first(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, after_node, data):
        if after_node is None:
            print("The given previous node cannot be NULL")
            return
        n = Node(data)
        n.next = after_node.next
        after_node.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_item(self, data):
        if self.start is None:
            return

        # Case when the node to delete is the first node
        if self.start.item == data:
            self.start = self.start.next
            return

        temp = self.start
        while temp.next is not None:
            if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def __iter__(self):
        return SLLiterator(self.start)

class SLLiterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# Example usage
mylist = SLL()
mylist.insert_at_first(20)
mylist.insert_at_last(60)
mylist.delete_item(60)
mylist.print_list()

# Search for a node containing 20 and insert 50 after it
node = mylist.search(20)
if node:
    mylist.insert_after(node, 50)

# Print the linked list
mylist.print_list()  # Output should be: 20 50 60
