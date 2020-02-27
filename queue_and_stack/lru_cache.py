from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # check if key is in cache
        print(26, key)
        print(27, self.storage)
        if key in self.storage:
            # retrieve the node with the value
            node = self.storage[key]
            print("in storage")
            self.order.move_to_end(node)
            # finall return the value
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # first we need to see if the key is in the cache
        print(49, self.limit, self.size)
        if key in self.storage:
            print("key in storage map")
            # getthe node out of the dll from the dict
            nodeToHandle = self.storage[key]
            print(53, nodeToHandle)
            nodeToHandle.value = (key, value)
            self.order.move_to_end(nodeToHandle)
            return            
        
        if self.size == self.limit:
            # pop the tail from the dll, grab the k/v
            del self.storage[self.order.head.value[0]]
      
            self.order.remove_from_head()
            self.size -= 1   
        
        self.order.add_to_tail((key,value))
        self.storage[key] = self.order.tail
        self.size += 1
        