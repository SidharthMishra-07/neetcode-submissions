class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)  
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size-=1

    def addToFront(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size+=1

    def remove_last(self):
        if self.tail.prev == self.head:
            return
        last = self.tail.prev
        self.remove(last)
        return last

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}     #KEY -> Node
        self.freqMap = {}   #FREQ -> DoublyLinkedList
        self.min_freq = 0

    #INCREMENT the freq of NODE when GET and PUT is called
    def increment_freq(self, node):
        old_list = self.freqMap[node.freq]
        old_list.remove(node)

        if old_list.size == 0:
            del self.freqMap[node.freq]
            if self.min_freq == node.freq:
                self.min_freq+=1
        node.freq +=1
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DoublyLinkedList()
        self.freqMap[node.freq].addToFront(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.increment_freq(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.increment_freq(node)
        else:
            if len(self.cache) == self.capacity:
                lfu_list = self.freqMap[self.min_freq]
                lfu = lfu_list.remove_last()
                del self.cache[lfu.key]
                if lfu_list.size == 0:
                    del self.freqMap[self.min_freq]

            new_node = Node(key, value)
            self.cache[key] = new_node
            if 1 not in self.freqMap:
                self.freqMap[1] = DoublyLinkedList()
            self.freqMap[1].addToFront(new_node)
            self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)