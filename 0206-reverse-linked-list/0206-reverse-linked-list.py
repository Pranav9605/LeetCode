# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None
        # newHead=Head
        # if head.next:
        #     newHead=self.reverseList(head.next)
        #     head.next.next=Head
        # head.next=None
        # return newHead




        # ------------------
        curr=head
        pre=None
        nxt=None
        while(curr):
            nxt=curr.next
            curr.next=pre
            pre=curr
            curr=nxt
        return pre