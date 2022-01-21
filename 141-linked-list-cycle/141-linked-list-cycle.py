# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head   
        if not head:
            return      
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True           
        return False
    #O(n) Time complexity
    #O(1) Space complexity
        