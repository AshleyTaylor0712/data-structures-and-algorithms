class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """

    """
    def __init__(self):
     self.head = None
     self.tail = None
     self.size = 0

    # this checks if the list in empty
    def is_empty(self):
      if self.head is None:
          return None

    #inserts a new value at the tail of linkedlist
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
           self.tail.next = new_node
           self.tail = new_node

        self.size += 1

    def __str__(self):
        if self.head is None:
            return "NULL"
        else:
            node = self.head
            values = []
            while node is not None:
                values.append("{ " + str(node.value) + " }")
                node = node.next
            values.append("NULL")
            return " -> ".join(values)


pass


class TargetError:
    pass

if __name__ == "__main__":
    linked = LinkedList()
    #linked.insert("apple")
    #print (linked.head.value)
    print (linked.__str__())
