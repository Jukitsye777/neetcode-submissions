# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupprev = dummy

        while(True):
            kth = groupprev
            for i in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next
            
            groupnext = kth.next

            prev = groupnext
            curr = groupprev.next

            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            
            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp

        return dummy.next