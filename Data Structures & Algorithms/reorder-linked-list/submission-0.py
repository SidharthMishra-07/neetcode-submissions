# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow  # node BEFORE mid

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        # 1️⃣ Find middle
        center = self.middle(head)

        # 2️⃣ Split list
        mid = center.next
        center.next = None

        # 3️⃣ Reverse second half
        head2 = self.reverse(mid)

        # 4️⃣ Merge alternately
        tail1 = head
        tail2 = head2

        while tail1 and tail2:
            temp1 = tail1.next
            temp2 = tail2.next

            tail1.next = tail2
            tail2.next = temp1

            tail1 = temp1
            tail2 = temp2