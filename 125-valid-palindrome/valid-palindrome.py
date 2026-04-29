class Solution(object):
    def isPalindrome(self, s):
        a=s.lower()
        b="".join(i for i in a if i.isalnum())
        d=b[::-1]
        if b==d:
            return True
        else:
            return False