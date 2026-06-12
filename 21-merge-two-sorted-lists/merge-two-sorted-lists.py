# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        l=list1
        l1=list2
        f=[]
        while l:
            f.append(l.val)
            l=l.next
        while l1:
            f.append(l1.val)
            l1=l1.next
        f.sort()
        c=ListNode(0)
        d=c
        for i in f:
            d.next=ListNode(i)
            d=d.next

        return c.next
        