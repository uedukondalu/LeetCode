# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1=""
        while l1:
            s1+=str(l1.val)
            l1=l1.next
        s2=""
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        t=int(s1[::-1])+int(s2[::-1])
        t1=list(str(t)[::-1])
        h=ListNode()
        head=h
        for i in t1:
            head.next=ListNode(int(i))
            head=head.next
        return h.next


        