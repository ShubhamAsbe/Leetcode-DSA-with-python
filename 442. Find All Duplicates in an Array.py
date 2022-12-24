class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        twice=[]
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                twice.append(nums[i])
        return twice