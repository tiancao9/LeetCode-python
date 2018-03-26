'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        if (n+m) % 2 != 0:
            return self.find_kth_num(nums1, 0, nums2, 0, int((n+m)/2+1))
        else:
            return (self.find_kth_num(nums1, 0, nums2, 0, int((n+m)/2)) + self.find_kth_num(nums1, 0, nums2, 0, int((n+m)/2+1))) / 2
        
#Define the fuction to find kth number of num1, nums2
    def find_kth_num(self,nums1, begin1, nums2, begin2, k):
        
        if begin1 >= len(nums1):
            return nums2[begin2+k-1]
        if begin2 >= len(nums2):
            return nums1[begin1+k-1]
        if k == 1:
            return min(nums1[begin1], nums2[begin2])
        
        if begin2 + int(k/2) - 1 >= len(nums2):
            return self.find_kth_num(nums1, int(begin1+int(k/2)), nums2, begin2, k - int(k/2))
        elif begin1 + int(k/2) - 1 >= len(nums1):
            return self.find_kth_num(nums1, begin1, nums2, int(begin2+int(k/2)), k - int(k/2))
                
        if nums1[begin1+int(k/2)-1] < nums2[begin2+int(k/2)-1]:
            return self.find_kth_num(nums1, int(begin1+int(k/2)), nums2, begin2, k - int(k/2))
        else:
            return self.find_kth_num(nums1, begin1, nums2, int(begin2+int(k/2)), k - int(k/2))
