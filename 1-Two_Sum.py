class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums): #How to use enumerate: http://book.pythontips.com/en/latest/enumerate.html
            if target - num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i;
        
        
