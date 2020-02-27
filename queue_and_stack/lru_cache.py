from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
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
        if key in self.storage.keys():
            # retrieve the node with the value
            node = self.storage
            print(node.values)
            # key/value pairs are stored in the nodes as tuples, thus access
            # the value here via get at first index (the key is at index zero
            value = node.values[1]
            # make a new node at the head and updatedict entry
            self.storage[key] = self.order.add_to_head((key, value))
            # delete the original node
            self.order.delete(node)
            # finall return the value
            return value
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
        if key in self.storage.keys():
            print("key in storage map")
            # getthe node out of the dll from the dict
            nodeToHandle = self.storage[key]
            # delete the node
            self.order.delete(nodeToHandle)
            # make a new node at the headand dict entry
            self.storage[key] = self.order.add_to_head((key, value))
        else:
            if self.size == self.limit:
                # pop the tail from the dll, grab the k/v
                # remove that key from the storage map
                keyToRemove: [] = self.order.remove_from_tail()
                self.storage.pop(keyToRemove[0], None)
                # add the new key to the storage map and to the dll
                self.storage[key] = self.order.add_to_head((key, value))
            else:
                # increment the current node count
                self.size += 1
                # add the key at the front of the list
                # and link the dict to the node
                self.storage[key] = self.order.add_to_head((key, value))
        