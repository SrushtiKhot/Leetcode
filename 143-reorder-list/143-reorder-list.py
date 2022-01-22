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
            
#We reach exactly half way of the linked list at slow.The second half starts slow.next

        second=slow.next 
    
        #Reverse the second half
        prev=None
        slow.next=None  #Make first list's last element.next=None to indicate end of list
        
        while(second):
            temp=second.next
            second.next=prev
            prev=second
            second=temp
            
        #first list's head and second list's head is initialized
        first=head
        second=prev   
        
        #Merge first and second sorted array
        while(first and second):
            temp1,temp2=first.next,second.next #Store next elements of first and second lists
            first.next=second                   #Make first element's next as second list's element
            second.next=temp1                   #Make second element's next as first list's element
            first,second=temp1,temp2            #To continue till end of lists
        return head
