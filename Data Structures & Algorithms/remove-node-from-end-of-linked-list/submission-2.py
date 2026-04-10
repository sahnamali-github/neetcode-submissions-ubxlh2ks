# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #reverse linedlist
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        #removed nth node
        manda = prev
        dummy = ListNode(0)
        tail = dummy
        count = 0
        curr = manda
        while curr:
            count += 1
            nxt = curr.next
            if count != n:
                tail.next = curr
                tail = tail.next
                tail.next = None
            curr = nxt
        #reverse dummy.next
        res = dummy.next
        prev, curr = None, res
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        




        