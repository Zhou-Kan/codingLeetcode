# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = 0
        hash_map = defaultdict(int)
        
        while head:
            if head in hash_map:
                return head
            
            hash_map[head] = pos
            pos += 1
            head = head.next
            
        return head
        