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
        if head == None:
            return None

        #step 1: interleave copy betwn original
        curr = head
        while curr:
            next = curr.next
            copy = Node(curr.val)
            curr.next = copy
            copy.next= next
            curr = next
        
        #step 2: random pointer for copy
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        #step 3:breaking bond betwn original and copy
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if curr.next:
                copy.next = curr.next.next
            curr = curr.next
        return copy_head
