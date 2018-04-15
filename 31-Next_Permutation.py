'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
# from n to 0, find the 1st decreasing number nums[i-1], from i to n, find the least number nums [j] that still > nums[i-1]
# swap nums[i-1] and nums[j]
# sort nums[i:]
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                j = i
                while j < len(nums) and nums[j] > nums[i-1]:
                    j += 1
                j = j - 1
                temp = nums[j]
                nums[j] = nums[i-1]
                nums[i-1] = temp
                break
            i -= 1
                
        nums[i:] = sorted(nums[i:])

