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

    def is_empty(self):
      return self.head is None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
           self.tail.next = new_node
           self.tail = new_node

        self.size += 1
        
def test_to_string_empty():
  linked_list = LinkedList()

  assert str(linked_list) == "NULL"


pass


class TargetError:
    pass
