'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
'''
#sort the list + 2 pointer 
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0;
        j = 0
        m = len(nums)-1
        nums.sort()
        data = []
        while j < len(nums):
            if j%2 == 0:
                data.append(nums[i])
                i += 1
            else:
                data.append(nums[m])
                m -= 1
            j += 1
        
        for i in range(len(nums)):
            nums[i]=data[i]
