'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

'''

# Binary search, to define while condition is left <= right, can try 3 element array 
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        left = 1
        right = len(nums)-2
        while(left <= right):
            mid = int(left + (right-left)/2)
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
        
        if nums[1] < nums[0]: 
            return 0
        else: 
            return len(nums)-1

