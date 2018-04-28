'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''

# scan from len(nums)-1 to i, insert nums[i] into res[], compare exising num in res, use binary search to find the target pos in res
# count[i] = target pos of nums[i] in res
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        count = [0] * len(nums)
        i = len(nums)-1
        while i >= 0:
            if len(res) == 0:
                res.append(nums[i])
                count[i] = 0
            else:
                left = 0
                right = len(res)-1
                while left < right:
                    mid = int(left + (right-left)/2)                    
                    if nums[i] <= res[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                if nums[i] <= res[left]:
                    count[i] = left
                    res.insert(left, nums[i]) #insert is much faster than res = res[:left] + [nums[i]] + res[left:]
                else:
                    count[i] = left+1
                    res.insert(left+1, nums[i])
            i -= 1
        return count

