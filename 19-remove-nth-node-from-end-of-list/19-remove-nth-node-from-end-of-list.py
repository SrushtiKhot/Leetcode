# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #First find the length
        temp=head
        length=0
        while(temp):
            temp=temp.next
            length+=1
            
        if length==n:
            return head.next
            
        temp=head
       
        for i in range(1,length-n):
            temp=temp.next
            
        temp.next=temp.next.next
        
        return head
    
            
            
            
        