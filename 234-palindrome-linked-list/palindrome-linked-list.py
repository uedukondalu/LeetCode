# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        f=[]
        curr=head
        while curr:
            f.append(curr.val)
            curr=curr.next
        if f==f[::-1]:
            return True
        return False