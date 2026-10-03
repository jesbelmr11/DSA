class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        arr=[]

        for i in range(m):
            arr.append(nums1.pop(0))
        nums1[:]=[]
        arr.extend(nums2)
        arr.sort()
        nums1.extend(arr)
        return nums1
        