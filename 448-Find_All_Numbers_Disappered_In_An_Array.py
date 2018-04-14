'''
Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
# for num in nums, mark pos num-1's number * -1
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

