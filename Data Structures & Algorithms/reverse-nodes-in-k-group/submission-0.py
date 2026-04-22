# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1: Check if we have at least k nodes
        curr = head
        cnt = 0
        while curr and cnt < k:
            curr = curr.next
            cnt += 1
        
        if cnt < k:
            return head

        curr = head
        prev = None
        temp = None
        count = 0

        # Step 2: Reverse first k nodes
        while curr and count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        
        # Step 3: Recursively reverse remaining list
        if temp != None:
            rest_head = self.reverseKGroup(temp, k)
            head.next = rest_head

        return prev