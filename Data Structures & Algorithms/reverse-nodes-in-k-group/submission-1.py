# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 
        cnt = 0
        curr = head
        
        #Check if K nodes are present or not
        while curr and cnt<k:
            curr = curr.next
            cnt+=1
        
        if cnt < k:
            return head
        
        #Reverse the first k nodes
        curr = head
        prev = None
        temp = None
        pos = 0
        while curr and pos < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            pos+=1

        if temp != None:
            new_head = self.reverseKGroup(temp, k)
            head.next = new_head
        
        return prev