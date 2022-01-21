# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head 
        if not head:
            return
        prev=None 

        while(temp):
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
            
        return(prev)
            
        
        
        