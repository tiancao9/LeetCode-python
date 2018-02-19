'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Sol1: use heap, O(nlog(n))
        #return [key for key, _ in collections.Counter(nums).most_common(k)]
        #Sol2: use extra list to record the list of num with same repeating numbers 
        count = collections.Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for i, c in count.items():
            bucket[c].append(i)
            
        result = []
        for i in reversed(range(len(bucket))):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result) == k:
                    return result 
