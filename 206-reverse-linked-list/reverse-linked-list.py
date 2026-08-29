# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        curr=head
        if curr and curr.next==None:
            return head
        prev=None
        ne=None
        curr=head
        while curr:
            ne=curr.next
            curr.next=prev
            prev=curr
            curr=ne
        return prev

        