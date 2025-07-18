# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        head.next = self.removeElements(head.next, val)        
        if head.val == val:
            head = head.next

        return head


        # if head is None:
        #     return head
        # prev=head
        # curr=head.next
        # while curr is not None:
        #     if curr.val==val:
        #         prev.next=curr.next
        #     else:
        #         prev=curr
        #     curr=curr.next
        # if head.val==val:
        #     return head.next
        
        # return head

                
            



        