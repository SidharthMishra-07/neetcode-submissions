class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.left = Node(0)     #DUMMY Head
        self.right = self.left

    def enQueue(self, value: int) -> bool:
        new_node = Node(value)
        if self.isFull():
            return False
        if self.isEmpty():
            self.left.next = new_node
            self.right = new_node
        else:
            self.right.next = new_node
            self.right = new_node
        self.size-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.size +=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.val

    def isEmpty(self) -> bool:
        return self.left.next == None

    def isFull(self) -> bool:
        return self.size==0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()