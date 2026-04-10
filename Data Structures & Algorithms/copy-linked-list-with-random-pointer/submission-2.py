"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Method 1 - two pass with hashmap
        #step 1: copy linkedlist, map original to copy
        # oldToCopy = {None:None}   #so that none will be pointed to none.
        # curr = head
        # while curr:
        #     copy = Node(curr.val)
        #     oldToCopy[curr] = copy
        #     curr = curr.next
        # #step2: connect pointers
        # curr = head
        # while curr:
        #     oldToCopy[curr].next = oldToCopy[curr.next]
        #     oldToCopy[curr].random = oldToCopy[curr.random]
        #     curr = curr.next
        # return oldToCopy[head]


        #method 2: without hashmap. Interleaving copy betwn the original
        
        if not head:
            return None

        # Step 1: interleave copy nodes
        cur = head
        while cur:
            nxt = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = nxt
            cur = nxt

        # Step 2: assign random pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Step 3: separate lists
        cur = head
        copy_head = head.next

        while cur:
            copy = cur.next
            cur.next = copy.next
            if cur.next:
                copy.next = cur.next.next
            cur = cur.next

        return copy_head
