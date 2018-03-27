'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits)-1
        data = []
        while i >= 0:
            cur = carry + digits[i]
            data.append(cur % 10)
            carry = int (cur / 10)
            i -= 1
        if carry:
            data.append(carry)
        data = data[::-1]
        return data
