# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=head
        if current is None:
            return False
        if current.next is None:
            return True
        stack=[]
        while current is not  None:
            stack.append(current.val)
            current=current.next
        current=head
        while current is not None:
            if current.val==stack.pop():
                current=current.next
            else:
                return False
        return True


        
        
        