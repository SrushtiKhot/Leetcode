# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Perform in 2 steps:
        #1) Reverse the second half
        #2)Merge first half and reveresed second half
        
        slow=head
        fast=head.next
        
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            
        second=slow.next
        
        #Reverse the second half
        prev=None
        slow.next=None
        while(second):
            temp=second.next
            second.next=prev
            prev=second
            second=temp
            
        first=head
        second=prev      
        #Merge first and second sorted array
        while(second):
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2    
        return head
