class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #helper func
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def moveToFirst(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeLast(self):
        if self.tail.prev == self.head:
            return 
        last = self.tail.prev
        self.remove(last)
        return last

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.moveToFirst(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.moveToFirst(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.removeLast()
                if lru:
                    del self.cache[lru.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.moveToFirst(new_node)
            


