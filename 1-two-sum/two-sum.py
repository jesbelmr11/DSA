class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            a=nums[i]
            needed=target-a

            if needed in nums:
                b=nums.index(needed)

                if b!=i:
                    return i,b
        