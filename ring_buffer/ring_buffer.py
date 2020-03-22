from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    ''' The `append` method adds elements to the buffer. '''
    def append(self, item):
        # If at max capacity, remove oldest entry
        if len(self.storage) == self.capacity:
            # delete the head (oldest node)
            self.storage.remove_from_head()

        # Add item to the ring buffer
        self.storage.add_to_tail(item)

    ''' The `get` method returns all of the elements in the buffer in a list in their given order. 
    It should not return any `None` values in the list even if they are present in the ring buffer. '''
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        # Check if not empty, add first node to list
        if not self.storage.head is None:
            self.current = self.storage.head
            list_buffer_contents.append(self.current.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
