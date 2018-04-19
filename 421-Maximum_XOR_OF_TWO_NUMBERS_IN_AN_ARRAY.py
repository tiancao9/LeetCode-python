'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''
# Find from bit 31, save the prefix (num>>i) into an unordered_set, find if res << 1 ^ 1 ^ prefix is in the s, if yes, res++ 
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int mask = 0;
        int res = 0;
        for(int i = 31; i >= 0; i--)
        {
            unordered_set<int> s;
            for(int num: nums)
                s.insert(num >> i);
            res <<= 1;
            for(int prefix: s)
                if(s.count(res^1^prefix))
                {
                    res++;
                    break;
                }
        }
        return res;
    }
};

