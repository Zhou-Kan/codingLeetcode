# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        dummy_node = ListNode(0, head)
        
        slow = fast = dummy_node 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        cur = slow.next
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        while prev:
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next
            
        return True
            
        
            
            
            
        
            
        
        