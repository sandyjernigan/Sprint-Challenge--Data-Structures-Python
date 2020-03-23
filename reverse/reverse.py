class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def __str__(self):
    curNode = self.head
    output = ''
    output += f'( {curNode.value} )'

    while curNode.next_node is not None:
      curNode = curNode.next_node
      output += f' -> ( {curNode.value} )'

    return output

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # if empty return None
    if self.head is None:
      return None

    # Get Current head node
    curNode = self.head
    count = 1

    # Iterate over list to get length
    while curNode.next_node is not None:
      curNode = curNode.next_node
      count += 1

    # Store previous head
    previous = self.head
    # This should be the last node, set this as the new head
    self.head = curNode
    # replace next node
    curNode.set_next(previous.next_node)

    
    


testList = LinkedList()

testList.add_to_head(1)
testList.add_to_head(2)
testList.add_to_head(3)

print(testList)

testList.reverse_list()