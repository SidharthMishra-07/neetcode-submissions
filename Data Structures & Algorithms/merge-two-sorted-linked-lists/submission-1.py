# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:  
        if not head1:
            return head2
        if not head2:
            return head1

        curr1 = head1
        curr2 = head2

        head = None

        if curr1.val <= curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        
        curr = head
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        if curr1:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next

        if curr2:
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next

        return head


