class Solution(object):
    def merge(self, nums1, m, nums2, n):
        f=[]
        for i in range(len(nums1)):
            if len(f)<m:
                f.append(nums1[i])
        f1=[]
        for i in range(len(nums2)):
            if len(f1)<n:
                f1.append(nums2[i])
        r=f+f1
        res=sorted(r)
        nums1[:]=res
        return nums1


        