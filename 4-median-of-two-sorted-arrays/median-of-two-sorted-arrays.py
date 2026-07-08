class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n=sorted(nums1+nums2)
        j=len(n)
        m=len(n)//2
        if j%2!=0:
            return n[m]
        else:
            return (n[m-1]+n[m])/2.0
