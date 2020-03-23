from doubly_linked_list import DoublyLinkedList


''' A ring buffer is a non-growable buffer with a fixed size. '''
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    ''' The `append` method adds elements to the buffer. '''
    def append(self, item):
        ''' When the ring buffer is full and a new element is inserted, 
            the oldest element in the ring buffer is overwritten with the newest element. '''   
        # If at max capacity, overwrite the oldest element
        if len(self.storage) == self.capacity:
            # set current to next item, which should be the oldest element
            # If at end of list go back to the beginning of the list
            if self.current.next is None:
                self.current = self.storage.head
            else: 
                self.current = self.current.next
            
            # Overwrite oldes element with item value
            self.current.value = item
        else: 
            # Add item to the ring buffer, if not at max capacity
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
       

    ''' The `get` method returns all of the elements in the buffer in a list in their given order. 
    It should not return any `None` values in the list even if they are present in the ring buffer. '''
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        # Check if not empty, add first node to list
        if not self.storage.head is None:
            curNode = self.storage.head
            list_buffer_contents.append(curNode.value)

            # While there is another node, append the node to the list
            while not curNode.next is None:
                curNode = curNode.next
                list_buffer_contents.append(curNode.value)

        return list_buffer_contents

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print (buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
