'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. 
'''
#Conside horizontally for each point, min(left_max, righ_max) - height[i]
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        if len(height) == 0: 
            return res
        left_max = len(height) * [height[0]]
        right_max = len(height) * [height[-1]]
        i = 1
        
        while i < len(height):
            left_max[i] = max(left_max[i-1], height[i-1])
            i += 1
        i = len(height)-2
        while i >= 0:
            right_max[i] = max(right_max[i+1], height[i+1])
            if height[i] < min(left_max[i], right_max[i]):
                res += min(left_max[i], right_max[i]) - height[i]
            i -= 1
        return res
